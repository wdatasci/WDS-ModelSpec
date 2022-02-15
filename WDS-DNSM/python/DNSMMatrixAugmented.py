
import sys
from numpy import *
from string import *
import gBound.gDNSMMatrix
import csv

def doubleifnull(arg1,arg2):
	if arg1=="":return float(arg2)
	else: return float(arg1)

def intifnull(arg1,arg2):
	if arg1=="":return int(arg2)
	else: return int(arg1)

class DNSMMatrixAugmented:
	DNSMMatrixGuts = None
	DNSMMatrix = None
	nstates=0
	naxes=0
	naxis1=0
	naxis2=0
	naxis3=0
	naxis4=0
	oaxis1=0
	oaxis2=0
	oaxis3=0
	oaxis4=0
	nrows=0
    	def __init__(self) :
		DNSMMatrixGuts = None
		DNSMMatrix = None
		nstates=0
		naxes=0
		naxis1=0
		naxis2=0
		naxis3=0
		naxis4=0
		nrows=0
	def showGuts(self):
		print self.DNSMMatrixGuts	
	def showGutsAt(self,i,j,k,l):
		print self.DNSMMatrixGuts[:,:,i,j,k,l]	

def parse(s,GutsAsCSV=False,nStatesAsDim1=True):
	rc=DNSMMatrixAugmented()
	if GutsAsCSV==False:
		rc.DNSMMatrix=gDNSMMatrix.parse(s)
	else:
		rc.DNSMMatrix=gDNSMMatrix.parse(join([s,"Header"],sep=''))
	rc.nstates=int(rc.DNSMMatrix.getNumberofstates())
	rc.naxes=int(rc.DNSMMatrix.getNumberofadditionalaxes())
	if rc.naxes>0:
		rc.naxis1=int(rc.DNSMMatrix.getAdditionalaxesupperlimits().getAxis1())
		rc.oaxis1=int(rc.DNSMMatrix.getAdditionalaxeslowerlimits().getAxis1())
	else:
		rc.naxis1=1
		rc.oaxis1=0
	if rc.naxes>1:
		rc.naxis2=int(rc.DNSMMatrix.getAdditionalaxesupperlimits().getAxis2())
		rc.oaxis2=int(rc.DNSMMatrix.getAdditionalaxeslowerlimits().getAxis2())
	else:
		rc.naxis2=1
		rc.oaxis2=0
	if rc.naxes>2:
		rc.naxis3=int(rc.DNSMMatrix.getAdditionalaxesupperlimits().getAxis3())
		rc.oaxis3=int(rc.DNSMMatrix.getAdditionalaxeslowerlimits().getAxis3())
	else:
		rc.naxis3=1
		rc.oaxis3=0
	if rc.naxes>3:
		rc.naxis4=int(rc.DNSMMatrix.getAdditionalaxesupperlimits().getAxis4())
		rc.oaxis4=int(rc.DNSMMatrix.getAdditionalaxeslowerlimits().getAxis4())
	else:
		rc.naxis4=1
		rc.oaxis4=0
	if rc.naxis1==0:
		rc.naxis1=1
		rc.oaxis1=0
	if rc.naxis2==0:
		rc.naxis2=1
		rc.oaxis2=0
	if rc.naxis3==0:
		rc.naxis3=1
		rc.oaxis3=0
	if rc.naxis4==0:
		rc.naxis4=1
		rc.oaxis4=0
	rc.nrows=rc.nstates
	if rc.naxes==0:
		rc.naxis1=1
		rc.naxis2=1
		rc.naxis3=1
		rc.naxis4=1
	elif rc.naxes==1:
		rc.nrows*=rc.naxis1
		rc.naxis2=1
		rc.naxis3=1
		rc.naxis4=1
	elif rc.naxes==2:
		rc.nrows*=rc.naxis1
		rc.nrows*=rc.naxis2
		rc.naxis3=1
		rc.naxis4=1
	elif rc.naxes==3:
		rc.nrows*=rc.naxis1
		rc.nrows*=rc.naxis2
		rc.nrows*=rc.naxis3
		rc.naxis4=1
	elif rc.naxes==4:
		rc.nrows*=rc.naxis1
		rc.nrows*=rc.naxis2
		rc.nrows*=rc.naxis3
		rc.nrows*=rc.naxis4
	if GutsAsCSV==False:
		if nStatesAsDim1:
			rc.DNSMMatrixGuts=zeros((rc.nstates,rc.nstates,rc.naxis1,rc.naxis2,rc.naxis3,rc.naxis4), double)
		for i1 in range(0,rc.naxis1):
			for i2 in range(0,rc.naxis2):
				for i3 in range(0,rc.naxis3):
					for i4 in range(0,rc.naxis4):
						for i in range(0,rc.nstates):
							md=rc.DNSMMatrix.getMdata()[rc.nstates*(i1+rc.naxis1*(i2+rc.naxis2*(i3+rc.naxis3*i4)))+i]
							for j in range(0,rc.nstates):
								if j==0:    rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol1()
								elif j==1:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol2()
								elif j==2:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol3()
								elif j==3:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol4()
								elif j==4:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol5()
								elif j==5:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol6()
								elif j==6:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol7()
								elif j==7:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol8()
								elif j==8:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol9()
								elif j==9:  rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol10()
								elif j==10: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol11()
								elif j==11: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol12()
								elif j==12: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol13()
								elif j==13: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol14()
								elif j==14: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol15()
								elif j==15: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol16()
								elif j==16: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol17()
								elif j==17: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol18()
								elif j==18: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol19()
								elif j==19: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol20()
								elif j==20: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol21()
								elif j==21: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol22()
								elif j==22: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol23()
								elif j==23: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol24()
								elif j==24: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol25()
								elif j==25: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol26()
								elif j==26: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol27()
								elif j==27: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol28()
								elif j==28: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol29()
								elif j==29: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol30()
								elif j==30: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol31()
								elif j==31: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol32()
								elif j==32: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol33()
								elif j==33: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol34()
								elif j==34: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol35()
								elif j==35: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol36()
								elif j==36: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol37()
								elif j==37: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol38()
								elif j==38: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol39()
								elif j==39: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol40()
								elif j==40: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol41()
								elif j==41: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol42()
								elif j==42: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol43()
								elif j==43: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol44()
								elif j==44: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol45()
								elif j==45: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol46()
								elif j==46: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol47()
								elif j==47: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol48()
								elif j==48: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol49()
								elif j==49: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol50()
								elif j==50: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol51()
								elif j==51: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol52()
								elif j==52: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol53()
								elif j==53: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol54()
								elif j==54: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol55()
								elif j==55: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol56()
								elif j==56: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol57()
								elif j==57: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol58()
								elif j==58: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol59()
								elif j==59: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol60()
								elif j==60: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol61()
								elif j==61: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol62()
								elif j==62: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol63()
								elif j==63: rc.DNSMMatrixGuts[i,j,i1,i2,i3,i4]=md.getCol64()
	else:
		csv_reader=csv.reader(open(join([s,"Guts.csv"],sep='')))
		row=csv_reader.next()
		if nStatesAsDim1:
			rc.DNSMMatrixGuts=zeros((rc.nstates,rc.nstates,rc.naxis1,rc.naxis2,rc.naxis3,rc.naxis4), double)
		else:
			rc.DNSMMatrixGuts=zeros((1,len(row)-5,rc.naxis1,rc.naxis2,rc.naxis3,rc.naxis4), double)
		for row in csv_reader:
			if row[0]<>"":
				for k in range(len(row)-5):
					rc.DNSMMatrixGuts[0,k,
						intifnull(row[1],0)-rc.oaxis1,
						intifnull(row[2],0)-rc.oaxis2,
						intifnull(row[3],0)-rc.oaxis3,
						intifnull(row[4],0)-rc.oaxis4]=doubleifnull(row[5+k],0.0)
	return rc


