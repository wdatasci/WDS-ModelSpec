#this is a very old form of the python Hats implementation, see WDS-Doc for updated notes

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

