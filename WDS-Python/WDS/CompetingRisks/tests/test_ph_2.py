
import numpy as np
import numpy.random as rand
import polars as pl
import math
from typing import *


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

data2=data2.with_column(pl.concat_list(['TestBaseline_1','Static_A','TV_A']).apply(lambda x: x[0]*np.exp(.3*x[1]+.2*x[2])).alias('Haz_A'))

data2=data2.with_column(pl.concat_list(['TestBaseline_2','Static_B','TV_A','TV_B']).apply(lambda x: x[0]*np.exp(.002*x[1]+.001*x[2]+.02*x[3])).alias('Haz_B'))

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







