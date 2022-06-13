
import sys
sys.path.append('./build')
from pyTestScalar import *
from pyTestScalar_guts import *


x=StaticObject()

x.A=3

x.B=5

print("x.A=",x.A,' x.B=',x.B," pyTestScalar_guts=",pyTestScalar_guts(x))

