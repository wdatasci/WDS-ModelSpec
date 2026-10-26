#this is a very old form of the python Hats implementation, see WDS-Doc for updated notes
'''Copyright (c) 2019-2027 Wypasek Data Science, Inc.
Released under the MIT open source license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import sys

from numpy import *


def fHatsNonMissing(arg, arg2, iHats=False):
	ncuts = len(arg2)
	nrows = 1 
	
	rc=zeros((nrows, ncuts),double)

	for i in range(nrows):

		tempval = float(arg) 
		tempdouble = tempval

		if tempdouble <= arg2[0]:
			if iHats:
				rc[i, 0] = tempdouble - arg2[0]
			else:
				rc[i, 0] = 1.0
		elif tempdouble >= arg2[-1]:
			if iHats:
				rc[i, -1] = tempdouble - arg2[-1]+(arg2[-1] - arg2[-2])/2.0
				for j in range(1,ncuts-1):
					rc[i, j] = (arg2[j+1] - arg2[j-1]) / 2.0
				rc[i, 0] = (arg2[1] - arg2[0]) / 2.0
			else:
				rc[i, -1] = 1.0
		else:
			if iHats:
				for j in range(ncuts-1):
					if j>1:
						if tempdouble>arg2[j]:
							tempdouble2=(arg2[j]-arg2[j-1]) / 2.0
							rc[i, j]+=tempdouble2
							rc[i, j-1]+=tempdouble2
					if tempdouble>arg2[j+1]:
						tempdouble2=(arg2[j+1]-arg2[j]) / 2.0
						rc[i, j+1]+=tempdouble2
						rc[i, j]+=tempdouble2
					elif tempdouble>arg2[j]:
						tempdouble2 = (tempdouble - arg2[j]) ** 2.0 / (arg2[j + 1] - arg2[j]) / 2.0
						rc[i, j+1]+=tempdouble2
						rc[i, j] = rc[i, j] + tempdouble - arg2[j] - tempdouble2
			else:
				for j in range(1,ncuts):
					if tempdouble > arg2[j-1] and tempdouble <= arg2[j]:
						tempdouble2 = (tempdouble - arg2[j-1]) / (arg2[j] - arg2[j-1])
						rc[i, j-1] = 1 - tempdouble2
						rc[i, j] = tempdouble2

	return rc


def fHats(arg, arg2, iHats=False, isMissing=False):
	ncuts = len(arg2)
	nrows = 1 
	

	if isMissing:
		rc=zeros((nrows, ncuts+1),double)
		rc[0,0]=1.0
		return rc

	rc=fHatsNonMissing(arg,arg2,iHats)
	rc=concatenate( ( mat([[0.0]]) , rc ) , 1 )
	return rc

