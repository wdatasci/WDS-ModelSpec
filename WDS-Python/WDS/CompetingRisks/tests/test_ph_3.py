
import numpy as np
import numpy.random as rand
import polars as pl
import math
import copy
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

data_static = pl.DataFrame({'ID':IDs,
            'N':[T for x in IDs],
            'VintageMonthID':[MonthID_Start+rand.randint(MonthID_Start,MonthID_Stop) for x in IDs],
            'Strata':rand.randint(0,2,M)+1,
            'Static_A':rand.rand(M),
            'Static_B':rand.rand(M)*100-30,
            })


data2 = Bones_explode(data_static, 
            RowCountName='N',
            RowIndexName='MonthID', 
            OffsetName="VintageMonthID",
            )

data2['TV_A'] = rand.rand(data2.shape[0])
data2['TV_B'] = 3*rand.rand(data2.shape[0])-2

data2['RowIndex'] = data2.MonthID-data2.VintageMonthID
data2['Age'] = data2.MonthID-data2.VintageMonthID


mdl = WDSModel("test_py_3", Responses=['Resp1', 'Resp2'])

vStatic_A = add_Variable(Model=mdl, Name='Static_A', CriticalValues=[.2, .6], CleanLimits=[.05, .95], Treatment='Hats', Coefficients=[[.3, 0, .8],[0.0, 0, 0.0]])
vStatic_A.add_DropIndex(1)
vStatic_A.VariableModelDirectives.Static = "Yes"
vStatic_A.VariableModelDirectives.ResponseUse = "Resp1"

vStatic_B= add_Variable(Model=mdl, Name='Static_B', CriticalValues=[-2, 20], CleanLimits=[-10, 40], Treatment='Hats', Coefficients=[[.3, .1, 0.0],[-.3, -.2, 0.0]])
vStatic_B.add_DropIndex(2)
vStatic_B.VariableModelDirectives.Static = "Yes"
vStatic_B.VariableModelDirectives.ResponseUse = "All"


vTV_A = add_Variable(Model=mdl, Name='TV_A', CriticalValues=[.2, .6], CleanLimits=[.05, .95], Treatment='Hats', Coefficients=[[.3, 0, .8],[-.3, 0, .17]])
vTV_A.add_DropIndex(1)
vTV_A.VariableModelDirectives.ResponseUse = "All"

vTV_B= add_Variable(Model=mdl, Name='TV_B', CriticalValues=[-2, 20], CleanLimits=[-10, 40], Treatment='Hats', Coefficients=[[0.0, 0.0, 0.0],[-.3, -.2, 0]])
vTV_B.add_DropIndex(2)
vTV_B.VariableModelDirectives.ResponseUse = "Resp2"

vTV_Age= add_Variable(Model=mdl, Name='TV_Age', CriticalValues=[0, 5, 10, 20, 100], CleanLimits=[-1, 110], Treatment='Hats', Coefficients=[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.1, 0.2, .1, -.1]])
vTV_Age.add_DropIndex(0)
vTV_Age.add_DropIndex(1)
vTV_Age.VariableModelDirectives.ResponseUse = "Resp2"



mdl_baseline = WDSModel("test_py_3_baseline", Responses=['All',])
vAge = add_Variable(Model=mdl_baseline, Name='Age', CriticalValues=[0.0, 10.0, 20.0, 80.0], CleanLimits=[-1.0, 140.0 ], Treatment='Hats', Coefficients=[[0.0, 0.0, 0.01, 0.012, 0.002]])
vAge.add_DropIndex(0)
vAge.add_DropIndex(1)




ModelBuildingMD = ModelBuildingMD_Constructor()(mdl)
arts_names = []
arts_droplist = []

baseline_arts = plDF(art_c.fArtificials(data2.Age+0.0,vAge.Treatment,vAge.CriticalValues.as_numpy(),vAge.CleanLimits.as_numpy(),LabelBase=vAge.Name))
baseline = plDF(art_c.fArtificialsScored(data2.Age+0.0,vAge.Treatment,vAge.CriticalValues.as_numpy(),vAge.CleanLimits.as_numpy(),vAge.CoefficientsSet.as_numpy(), LabelBase = vAge.Name + '_Marg'))

system_matrix_Resp1 = None
system_matrix_Resp2 = None
Static_A_arts = fArtificials(data2.Static_A,vStatic_A)
Static_A_marg = fArtificialsScored(data2.Static_A,vStatic_A)

system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vStatic_A.get_VariableModelDirectives().ResponseUse,Static_A_arts, system_matrix_Resp1, system_matrix_Resp2)
ModelBuildingMD.add_arts(vStatic_A, Static_A_arts.columns)

Static_B_arts = fArtificials(data2.Static_B,vStatic_B)
Static_B_marg = fArtificialsScored(data2.Static_B,vStatic_B)
    
ModelBuildingMD.add_arts(vStatic_B, Static_B_arts.columns)
system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vStatic_B.get_VariableModelDirectives().ResponseUse,Static_B_arts, system_matrix_Resp1, system_matrix_Resp2)

TV_A_arts = fArtificials(data2.TV_A,vTV_A)
TV_A_marg = fArtificialsScored(data2.TV_A,vTV_A)

ModelBuildingMD.add_arts(vTV_A, TV_A_arts.columns)
system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vTV_A.get_VariableModelDirectives().ResponseUse,TV_A_arts, system_matrix_Resp1, system_matrix_Resp2)

TV_B_arts = fArtificials(data2.TV_B,vTV_B)
TV_B_marg = fArtificialsScored(data2.TV_B,vTV_B)

ModelBuildingMD.add_arts(vTV_B, TV_B_arts.columns)
system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vTV_B.get_VariableModelDirectives().ResponseUse,TV_B_arts, system_matrix_Resp1, system_matrix_Resp2)

ebz = ((Static_A_marg + Static_B_marg + TV_A_marg + TV_B_marg)).with_columns(pl.col('*').apply(np.exp))  #*baseline[:,0]

data2['Haz_A'] = ebz[:,0]*baseline[:,0]
data2['Haz_B'] = ebz[:,1]*baseline[:,0]

fid = open(__file__+'.out','w')

mdl.export(fid, level=0)

fid.close()


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

data2=data2.join(x,on=['ID'])
#.filter(pl.col('RowIndex') <= pl.col('EventIndex'))
ind = data2.RowIndex <= data2.EventIndex

#data2_Resp1 = system_matrix.select(ModelBuildingMD.effective_names('Resp1'))
#data2_Resp2 = system_matrix.select(ModelBuildingMD.effective_names('Resp2'))


fid = open(__file__+'.out','w')

mdl.export(fid, level=0)

fid.close()




data=data2[ind]
system_matrix_Resp1 = system_matrix_Resp1[ind]
system_matrix_Resp2 = system_matrix_Resp2[ind]

fid = open(__file__+'.out.data.csv','w')
fid.write(data.to_csv())
fid.close()

fid = open(__file__+'.out.system_matrix_Resp1.csv','w')
fid.write(system_matrix_Resp1.to_csv())
fid.close()

fid = open(__file__+'.out.system_matrix_Resp2.csv','w')
fid.write(system_matrix_Resp2.to_csv())
fid.close()

fid = open(__file__+'.out.system_etc.csv','w')
fid.write(data.select(['ID','VintageMonthID','MonthID','Age','Signal','EventIndex']).to_csv())
fid.close()



