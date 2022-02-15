from numpy import *


def RowNormIt(arg1,m1,n1):
	rc=zeros((m1,n1),double)
	for i in range(m1):
		s=0.0000000
		for j in range(n1):
			s+=float(arg1[i,j])
			rc[i,j]+=float(arg1[i,j])
		if s<=0.0:s=1.0
		for j in range(n1):
			rc[i,j]/=s
	return rc
		
			







