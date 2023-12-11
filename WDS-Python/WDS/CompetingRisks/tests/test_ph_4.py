import numpy as np
import numpy.random as rand

import polars as pl

#newer polars does not allow df.x anymore, add a monkey patch for it
try:
    d=pl.DataFrame({a:[1,2], b:[3,4]})
    d.a
    def __monkey__filter__(self,a):
        return self[a]
    pl.DataFrame.mfilter = __monkey__filter__
    def add_column(df, name, value):
        df[name]=pl.Series(value)
        return df
except:
    def __monkey__getattr__(self,name):
       if name in self.columns:
         return self[name]
    pl.DataFrame.__getattr__ = __monkey__getattr__
    pl.DataFrame.to_csv = pl.DataFrame.write_csv
    pl.DataFrame.distinct = pl.DataFrame.unique
    def __monkey__matmul__(self,a):
        return self.to_numpy() @ a.to_numpy()
    pl.DataFrame.__matmul__ = __monkey__matmul__
    pl.DataFrame.mfilter = pl.DataFrame.filter
    def add_column(df, name, value):
        return df.with_column(pl.Series(value).alias(name))

def copy_with_column(df, name, value):
    return df.with_column(pl.Series(value.flatten()).alias(name))
    
import math
import copy
from typing import *

import WDS.Comp.ArtificialsCythonWrapped as art_c

from WDS.Comp.WDSModelPrep import *

from WDS.history import *
history_init(globals())
pl.cfg.Config.set_tbl_cols(20)
pl.cfg.Config.set_tbl_rows(20)

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
            'StrataID':rand.randint(0,2,M)+1,
            'Static_A':rand.rand(M),
            'Static_B':rand.rand(M)*100-30,
            })


data2 = Bones_explode(data_static, 
            RowCountName='N',
            RowIndexName='MonthID', 
            OffsetName="VintageMonthID",
            )

#data2['TV_A'] = rand.rand(data2.shape[0])
data2=add_column(data2,'TV_A',rand.rand(data2.shape[0]))
#data2['TV_B'] = 3*rand.rand(data2.shape[0])-2
data2=add_column(data2,'TV_B',50*rand.rand(data2.shape[0])-20)

#data2['RowIndex'] = data2.MonthID-data2.VintageMonthID
data2=add_column(data2,'RowIndex',data2.MonthID-data2.VintageMonthID)
#data2['Age'] = data2.MonthID-data2.VintageMonthID
data2=add_column(data2,'Age',data2.MonthID-data2.VintageMonthID)



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
vAge = add_Variable(Model=mdl_baseline, Name='Age', CriticalValues=[0.0, 10.0, 15.0, 30.0, 80.0], CleanLimits=[-1.0, 140.0 ], Treatment='BZ2',
Coefficients=[[0.0, 0.0, 0.1, 0.2, 0.08]])
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

system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vStatic_A,Static_A_arts, system_matrix_Resp1, system_matrix_Resp2)
ModelBuildingMD.add_arts(vStatic_A, Static_A_arts.columns)

Static_B_arts = fArtificials(data2.Static_B,vStatic_B)
Static_B_marg = fArtificialsScored(data2.Static_B,vStatic_B)
    
ModelBuildingMD.add_arts(vStatic_B, Static_B_arts.columns)
system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vStatic_B,Static_B_arts, system_matrix_Resp1, system_matrix_Resp2)

TV_A_arts = fArtificials(data2.TV_A,vTV_A)
TV_A_marg = fArtificialsScored(data2.TV_A,vTV_A)

ModelBuildingMD.add_arts(vTV_A, TV_A_arts.columns)
system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vTV_A,TV_A_arts, system_matrix_Resp1, system_matrix_Resp2)

TV_B_arts = fArtificials(data2.TV_B,vTV_B)
TV_B_marg = fArtificialsScored(data2.TV_B,vTV_B)

ModelBuildingMD.add_arts(vTV_B, TV_B_arts.columns)
system_matrix_Resp1, system_matrix_Resp2 = fAddToSystem(vTV_B,TV_B_arts, system_matrix_Resp1, system_matrix_Resp2)

ebz = ((Static_A_marg + Static_B_marg + TV_A_marg + TV_B_marg)).with_columns(pl.col('*').apply(np.exp))  #*baseline[:,0]

#data2['Haz_A'] = ebz[:,0]*baseline[:,0]
data2=add_column(data2,'Haz_A', ebz[:,0]*baseline[:,0])
#data2['Haz_B'] = ebz[:,1]*baseline[:,0]
data2=add_column(data2,'Haz_B',ebz[:,1]*baseline[:,0])

fid = open(__file__+'.out','w')

mdl.export(fid, level=0)

fid.close()


#data2['eps_A'] = rand.rand(data2.shape[0])
data2=add_column(data2,'eps_A',rand.rand(data2.shape[0]))
#data2['eps_B'] = rand.rand(data2.shape[0])
data2=add_column(data2,'eps_B',rand.rand(data2.shape[0]))

#data2['Signal_A']=data2.eps_A<data2.Haz_A
data2=add_column(data2,'Signal_A',data2.eps_A<data2.Haz_A)
#data2['Signal_B']=data2.eps_B<data2.Haz_B
data2=add_column(data2,'Signal_B',data2.eps_B<data2.Haz_B)

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
#ind = (pl.col('RowIndex') <= pl.col('EventIndex'))
ind = data2.RowIndex <= data2.EventIndex

#data2_Resp1 = system_matrix.select(ModelBuildingMD.effective_names('Resp1'))
#data2_Resp2 = system_matrix.select(ModelBuildingMD.effective_names('Resp2'))


fid = open(__file__+'.out','w')

mdl.export(fid, level=0)

fid.close()




data=data2.mfilter(ind)
system_matrix_Resp1 = data.select(['ID','StrataID','MonthID','Age','Signal']).hstack(system_matrix_Resp1.mfilter(ind))
system_matrix_Resp2 = data.select(['ID','StrataID','MonthID','Age','Signal']).hstack(system_matrix_Resp2.mfilter(ind))

data = data.sort(['StrataID','Age','Signal'])
system_matrix_Resp1 = system_matrix_Resp1.sort(['StrataID','Age','Signal'])
system_matrix_Resp2 = system_matrix_Resp2.sort(['StrataID','Age','Signal'])

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
fid.write(data.select(['ID','StrataID','MonthID','Age','Signal','EventClass','EventIndex']).to_csv())
fid.close()

#etc - events timed and classed
#names in common to all subjects
#  ID - unique subject
#  StrataID - common denominator grouping
#  Age - general subject age
#  Signal - etc class

base_names=['ID','StrataID','MonthID','Age','Signal']

Resp1_Names = copy.copy(base_names)
Resp1_Names.extend(ModelBuildingMD.effective_names('Resp1'))

Resp2_Names = copy.copy(base_names)
Resp2_Names.extend(ModelBuildingMD.effective_names('Resp2'))


Resp_Names = [ []
    , ModelBuildingMD.effective_names('Resp1')
    , ModelBuildingMD.effective_names('Resp2')
    ]
base_and_Resp_Names = [ []
    , Resp1_Names
    , Resp2_Names
    ]

#modeling indexed names
Resp_NamesPrefxd = [ [], [], [], ]
Resp_NamesX = [ [], [], [], ]
Resp_NamesXd = [ [], {}, {}, ]
for i in range(1,3):
    for nm2 in Resp_Names[i]:
        Resp_NamesXd[i][nm2]=[]
        Resp_NamesPrefxd[i].append('Resp'+str(i)+'_'+nm2)
    for nm2 in Resp_Names[i]:
        for nm1 in Resp_Names[i]:
            Resp_NamesX[i].append(nm1+'x'+nm2)
            Resp_NamesXd[i][nm2].append(nm1+'x'+nm2)

x1 = system_matrix_Resp1.select(base_and_Resp_Names[1]).lazy()
for i,nm in enumerate(Resp_Names[1]):
    x1=x1.with_columns((pl.col(Resp_Names[1])*pl.col(nm)).suffix('x'+nm))
x2 = system_matrix_Resp2.select(base_and_Resp_Names[2]).lazy()
for i,nm in enumerate(Resp_Names[2]):
    x2=x2.with_columns((pl.col(Resp_Names[2])*pl.col(nm)).suffix('x'+nm))

system_matrix = [ []
    , x1.collect() #system_matrix_Resp1.select(base_and_Resp_Names[1])
    , x2.collect() #system_matrix_Resp2.select(base_and_Resp_Names[2]) 
    ]

etc_and_base_names = copy.copy(base_names)

etc_and_base = data.select(etc_and_base_names).sort(['Signal','StrataID','Age'])

#unique index values
etc_denom_index = etc_and_base.mfilter(etc_and_base.Signal>0).select(['StrataID','Age','Signal']).distinct().sort(['StrataID','Age','Signal'])

#counts split by signal
Mn = [ etc_and_base.filter(pl.col('Signal')==0).shape[0]
    , etc_and_base.filter(pl.col('Signal')==1).shape[0]
    , etc_and_base.filter(pl.col('Signal')==2).shape[0]
    ]

#counts any signal by strata and age
MnSA=etc_and_base.filter(pl.col('Signal')>0).groupby(['StrataID','Age']).agg(pl.col('Signal').count().alias('M')).sort(['StrataID','Age'])

#counts by signal strata and age
#MnSA = [ etc_and_base.filter(pl.col('Signal')==0).groupby(['StrataID','Age']).agg([pl.col('ID').count()]).sort(['StrataID','Age'])
#    , etc_and_base.filter(pl.col('Signal')==1).groupby(['StrataID','Age']).agg([pl.col('ID').count()]).sort(['StrataID','Age'])
#    , etc_and_base.filter(pl.col('Signal')==2).groupby(['StrataID','Age']).agg([pl.col('ID').count()]).sort(['StrataID','Age'])
#    ]

#number of betas, {\em survival} state is index 0
nbeta=[0
    , len(ModelBuildingMD.effective_names('Resp1'))
    , len(ModelBuildingMD.effective_names('Resp2'))
    ]

nbetatotal=nbeta[0]+nbeta[1]+nbeta[2]


beta=[ []
    , pl.DataFrame(np.random.rand(nbeta[1],1))
    , pl.DataFrame(np.random.rand(nbeta[2],1))
    ]

for aaa in range(0,20):
    ebz=[ []
        , system_matrix[1].select(Resp_Names[1]) @ beta[1]
        , system_matrix[2].select(Resp_Names[2]) @ beta[2] 
        ]
    ebzc = ebz[1]+ebz[2]
    etcWebzc = copy_with_column(etc_and_base, 'ebzc', ebzc)
    
    etcWebz = [ []
        , copy_with_column(etcWebzc, 'ebz', ebz[1])
        , copy_with_column(etcWebzc, 'ebz', ebz[2]) 
        ]

    iter_comp_1 = [ []
        , system_matrix[1].filter(pl.col('Signal')==1).select(Resp_Names[1]).sum()
        , system_matrix[2].filter(pl.col('Signal')==2).select(Resp_Names[2]).sum()
        ]
    iter_comp_12 = [ [], [], [] ]
    
    iter_comp_2 = [ [], [], [] ]
    iter_comp_22 = [ [], [], [] ]
    
    x = (etcWebz[1].hstack(system_matrix[1].select([*Resp_Names[1],*Resp_NamesX[1]]) * etcWebz[1].ebz)).groupby(['StrataID','Age']).agg(pl.col(['ebz', 'ebzc', *Resp_Names[1], *Resp_NamesX[1]]).sum()).sort(['StrataID','Age'])
    xx = x.join(MnSA, on=['StrataID','Age'], how='inner')
    
    iter_comp_12[1] = (xx.select(Resp_Names[1]) * xx.M / xx.ebzc).sum()

    iter_comp_2[1] = (xx.select([*Resp_Names[1],*Resp_NamesX[1]]) * xx.M / xx.ebzc).sum()
    iter_comp_22[1] = (xx.select(Resp_Names[1]) * xx.M.apply(np.sqrt) / xx.ebzc) #.sum()
    
    x = (etcWebz[2].hstack(system_matrix[2].select([*Resp_Names[2],*Resp_NamesX[2]]) * etcWebz[2].ebz)).groupby(['StrataID','Age']).agg(pl.col(['ebz', 'ebzc', *Resp_Names[2], *Resp_NamesX[2]]).sum()).sort(['StrataID','Age'])
    xx = x.join(MnSA, on=['StrataID','Age'], how='inner')
    
    iter_comp_12[2] = (xx.select(Resp_Names[2]) * xx.M / xx.ebzc).sum()

    iter_comp_2[2] = (xx.select([*Resp_Names[2],*Resp_NamesX[2]]) * xx.M / xx.ebzc).sum()
    iter_comp_22[2] = (xx.select(Resp_Names[2]) * xx.M.apply(np.sqrt) / xx.ebzc) #.sum()
    
    
    
    betas = beta[1].vstack(beta[2])
    db=iter_comp_1[1].transpose().vstack(iter_comp_1[2].transpose())- iter_comp_12[1].transpose().vstack(iter_comp_12[2].transpose())

    db20agg = None
    for i in range(0,MnSA.shape[1]):
        db2_10 = iter_comp_22[1][i].select(Resp_Names[1]).transpose().vstack(iter_comp_22[2][i].select(Resp_Names[2]).transpose())
        db20 = (db2_10 @ db2_10.transpose())
        db20agg = db20*MnSA[i].M[0] + ( db20agg if db20agg is not None else 0 )

    k = -1
    sc = 0
    bdi=[ [],[],[]]
    for i in range(1,3):
        nnm = len(Resp_Names[i])
        for j,nm in enumerate(Resp_Names[i]):
            k+=1
            x = iter_comp_2[i].lazy()
            x = x.select(Resp_NamesXd[i][nm])
            for l,lnm in enumerate(Resp_NamesXd[i][nm]):
                x = x.with_column(pl.col(lnm).alias(Resp_NamesPrefxd[i][l]))
            if j==0:
                bdi[i] = x.select(Resp_NamesPrefxd[i]).collect()
            else:
                bdi[i] = bdi[i].vstack(x.select(Resp_NamesPrefxd[i]).collect())
            #db2[k, (sc):(sc+nnm)] -= x.to_numpy().reshape((1,nnm))
        sc+=nnm
    
    
    db2=bdi[1].hstack(bdi[2]*0).vstack((bdi[1]*0).hstack(bdi[2]))*(-1)+pl.DataFrame(db20agg)
    
    print(-np.linalg.inv(db2.to_numpy()))
    delta_betas= -np.linalg.inv(db2.to_numpy()) @ db.to_numpy()
    betas=betas+pl.DataFrame(delta_betas)
    sc=0
    for i in range(1,3):
        nnm=len(Resp_Names[1])
        beta[i]=betas[sc:sc+nnm]
        sc+=nnm

    print(betas)
    #break
    





