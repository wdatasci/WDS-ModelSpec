
import numpy as np
import numpy.random as rand
import polars as pl
import math
from typing import *

import WDS.Comp.ArtificialsCythonWrapped as art_c

from WDS.Comp.WDSModelPrep import *

from WDS.history import *
history_init(globals())

#build a model spec from scratch

def Bones_explode(df : pl.DataFrame,
        /,
        RowCountName : str = "N",
        RowIndexName : str = 'RowIndex',
        OffsetName : str = 'RowIndex_First',
        ) -> pl.DataFrame:
    rv = df.select([pl.col('*'),pl.concat_list([pl.col(OffsetName),pl.col(RowCountName)]).alias(RowIndexName)])
    rv = rv.with_column(pl.col(RowIndexName).apply(lambda x:[i+x[0] for i in range(0,x[1]+1)])).explode(RowIndexName)
    return rv

def Bones(ID_List : List[int],
        N_List   : List[int],
        Offset_List  :   List[int],
        /,
        IDName : str = 'ID',
        RowIndexName : str = 'RowIndex',
        OffsetName : str = 'RowIndex_First',
        ) -> pl.DataFrame:
    rv = pl.DataFrame({IDName:ID_List, 'N':N_List, OffsetName:Offset_List})
    return Bones_explode(rv, RowIndexName=RowIndexName, OffsetName=OffsetName)

MonthID_Start = (2020-2000)*12+1
MonthID_Stop = (2022-2000)*12+5

M = 1000

T = 100

IDs=[x for x in range(1, M+1)]

data = pl.DataFrame({'ID':IDs,
            'N':[T for x in IDs],
            'VintageMonthID':[MonthID_Start+rand.randint(MonthID_Start,MonthID_Stop) for x in IDs],
            'Strata':rand.randint(0,2,M)+1,
            'Static_A':rand.rand(M),
            'Static_B':rand.rand(M)*100-30,
            })


data2 = Bones_explode(data, 
            RowCountName='N',
            RowIndexName='MonthID', 
            OffsetName="VintageMonthID",
            )

data2['TV_A'] = rand.rand(data2.shape[0])
data2['TV_B'] = 3*rand.rand(data2.shape[0])-2

data2['RowIndex'] = data2.MonthID-data2.VintageMonthID
data2['Age'] = data2.MonthID-data2.VintageMonthID

data2['TestBaseline_1'] = data2.Age.apply(lambda x: np.exp(-np.power(x-10.0,2.0)/20.0)/100.0+x/1000.0+.002)
data2['TestBaseline_2'] = data2.Age.apply(lambda x: np.exp(-np.power(x-20.0,2.0)/40.0)/100.0+x/500.0+.001)



mdl = WDSModel("test_py_3", Responses=['Resp1', 'Resp2'])

vStatic_A = add_Variable(Model=mdl, Name='Static_A', CriticalValues=[.2, .6], CleanLimits=[.05, .95], Treatment='Hats', Coefficients=[[.3, 0, .8],[-.3, 0, .17]])
vStatic_A.add_DropIndex(1)
vStatic_A.VariableModelDirectives.Static = "Yes"
vStatic_A.VariableModelDirectives.ResponseUse = "Resp1"

vStatic_B= add_Variable(Model=mdl, Name='Static_B', CriticalValues=[-2, 20], CleanLimits=[-10, 40], Treatment='Hats', Coefficients=[[.3, .1, 0.0],[-.3, -.2, 0.0]])
vStatic_B.add_DropIndex(2)
vStatic_B.VariableModelDirectives.Static = "Yes"
vStatic_B.VariableModelDirectives.ResponseUse = "Resp2"


vTV_A = add_Variable(Model=mdl, Name='TV_A', CriticalValues=[.2, .6], CleanLimits=[.05, .95], Treatment='Hats', Coefficients=[[.3, 0, .8],[-.3, 0, .17]])
vTV_A.add_DropIndex(1)
vTV_A.VariableModelDirectives.ResponseUse = "All"

vTV_B= add_Variable(Model=mdl, Name='TV_B', CriticalValues=[-2, 20], CleanLimits=[-10, 40], Treatment='Hats', Coefficients=[[.3, .1, 0],[-.3, -.2, 0]])
vTV_B.add_DropIndex(2)
vTV_B.VariableModelDirectives.ResponseUse = "Resp2"


mdl_baseline = WDSModel("test_py_3_baseline", Responses=['All',])
vAge = add_Variable(Model=mdl_baseline, Name='Age', CriticalValues=[0.0, 10.0, 20.0, 80.0], CleanLimits=[-1.0, 140.0 ], Treatment='Hats', Coefficients=[[0.0, 0.0, 0.1, 0.08, 0.2]])
vAge.add_DropIndex(0)
vAge.add_DropIndex(1)

#baseline.view(dtype=np.float64,type=np.ndarray) @ vAge.Coefficients_as_numpy().T

baseline_arts = art_c.fArtificials(data2.Age+0.0,vAge.Treatment,vAge.CriticalValues.as_numpy(),vAge.CleanLimits.as_numpy(),LabelBase=vAge.Name)
baseline = art_c.fArtificialsScored(data2.Age+0.0,vAge.Treatment,vAge.CriticalValues.as_numpy(),vAge.CleanLimits.as_numpy(),vAge.CoefficientsSet.as_numpy(), LabelBase = vAge.Name + '_Marg')

system_matrix = pl.DataFrame(baseline_arts.view(dtype=np.float64),columns=baseline_arts.dtype.fields)

Static_A_arts = art_c.fArtificials(data2.Static_A,vStatic_A.Treatment,vStatic_A.CriticalValues.as_numpy(),vStatic_A.CleanLimits.as_numpy(), LabelBase =  vStatic_A.Name)
Static_A_marg = art_c.fArtificialsScored(data2.Static_A,vStatic_A.Treatment,vStatic_A.CriticalValues.as_numpy(),vStatic_A.CleanLimits.as_numpy(),vStatic_A.CoefficientsSet.as_numpy())
system_matrix.hstack(pl.DataFrame(Static_A_arts.view(dtype=np.float64),columns=Static_A_arts.dtype.fields), in_place=True)

Static_B_arts = art_c.fArtificials(data2.Static_B,vStatic_B.Treatment,vStatic_B.CriticalValues.as_numpy(),vStatic_B.CleanLimits.as_numpy(), LabelBase =  vStatic_B.Name)
Static_B_marg = art_c.fArtificialsScored(data2.Static_B,vStatic_B.Treatment,vStatic_B.CriticalValues.as_numpy(),vStatic_B.CleanLimits.as_numpy(),vStatic_B.CoefficientsSet.as_numpy())
system_matrix.hstack(pl.DataFrame(Static_B_arts.view(dtype=np.float64),columns=Static_B_arts.dtype.fields), in_place=True)

TV_A_arts = art_c.fArtificials(data2.TV_A,vTV_A.Treatment,vTV_A.CriticalValues.as_numpy(),vTV_A.CleanLimits.as_numpy(), LabelBase = vTV_A.Name)
TV_A_marg = art_c.fArtificialsScored(data2.TV_A,vTV_A.Treatment,vTV_A.CriticalValues.as_numpy(),vTV_A.CleanLimits.as_numpy(),vTV_A.CoefficientsSet.as_numpy())
system_matrix.hstack(pl.DataFrame(TV_A_arts.view(dtype=np.float64),columns=TV_A_arts.dtype.fields), in_place=True)

TV_B_arts = art_c.fArtificials(data2.TV_B,vTV_B.Treatment,vTV_B.CriticalValues.as_numpy(),vTV_B.CleanLimits.as_numpy(), LabelBase = vTV_B.Name)
TV_B_marg = art_c.fArtificialsScored(data2.TV_B,vTV_B.Treatment,vTV_B.CriticalValues.as_numpy(),vTV_B.CleanLimits.as_numpy(),vTV_B.CoefficientsSet.as_numpy())
system_matrix.hstack(pl.DataFrame(TV_B_arts.view(dtype=np.float64),columns=TV_B_arts.dtype.fields), in_place=True)

ebz = np.exp(Static_A_marg.view(dtype=np.float64)+TV_A_marg.view(dtype=np.float64))
data2['Haz_A'] = (ebz[:,0].reshape((ebz.shape[0],1))*baseline.view(dtype=np.float64)).flatten()
data2['Haz_B'] = (ebz[:,1].reshape((ebz.shape[0],1))*baseline.view(dtype=np.float64)).flatten()

#data2=data2.with_column(pl.concat_list(['TestBaseline_1','Static_A','TV_A']).apply(lambda x: x[0]*np.exp(.3*x[1]+.2*x[2])).alias('Haz_A'))
#data2=data2.with_column(pl.concat_list(['TestBaseline_2','Static_B','TV_A','TV_B']).apply(lambda x: x[0]*np.exp(.002*x[1]+.001*x[2]+.02*x[3])).alias('Haz_B'))

data2['eps_A'] = rand.rand(data2.shape[0])
data2['eps_B'] = rand.rand(data2.shape[0])

data2['Signal_A']=data2.eps_A<data2.Haz_A
data2['Signal_B']=data2.eps_B<data2.Haz_B

data2=data2.with_column(pl.concat_list(['Signal_A','Signal_B']).apply(lambda x: 1 if x[0] else 2 if x[1] else 0).alias('Signal'))

def f(arg):
    found=False
    for i,v in enumerate(arg):
        if v!=0:
            found=True
            break
    return i

x=data2.select(['ID','Signal']).groupby('ID').agg_list().select(['ID','Signal',pl.col('Signal').apply(f).alias('EventIndex')])
x=x.select(['ID','EventIndex',pl.concat_list(['Signal','EventIndex']).apply(lambda x:x[x[-1]]).alias('EventClass')])

data2=data2.join(x,on=['ID']).filter(pl.col('RowIndex') <= pl.col('EventIndex'))


fid = open(__file__+'.out','w')

mdl.export(fid, level=0)

fid.close()

vrbl = mdl.get_Variable('Static_A')

x1 = art_c.fArtificials(data2.Static_A,'Hats',vrbl.CriticalValues.as_numpy(),vrbl.CleanLimits.as_numpy())





