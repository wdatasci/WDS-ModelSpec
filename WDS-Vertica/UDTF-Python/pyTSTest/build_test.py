
import sys
sys.path.append('./build')
from pyTSTest import *
from pyTSTest_Enums import *


x=ExState.A

print(x)

print(x.bIn(ExState.Z))

print(x.bIn(ExState.Z,ExState.A))







