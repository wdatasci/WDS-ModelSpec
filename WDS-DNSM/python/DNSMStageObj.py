
import sys
from string import *
#from scipy import *
from array import array


import gBound.gDNSMFID
import gBound.gDNSMStateSpaceSpec
import gBound.gDNSMStocksAndFlowsSpec
import gBound.gDNSMMatrix
import gBound.gDNSMatrixAugmented

class StageObj:
	Name=None
	FID=None
	Topology=None
	ModelSpec=None
	BaseCounts=None
	BaseOdds=None
	BaseBalance=None
	BaseBalanceBias=None
	def __init__(self):
		self.Name=None
		self.FID=None
		self.Topology=None
		self.ModelSpec=None
		self.BaseCounts=None
		self.BaseOdds=None
		self.BaseBalance=None
		self.BaseBalanceBias=None

	def showGutsAt(self,i,j,k,l):
		print self.Name,"FID:"
		print self.Name,"Topology:"
		self.Topology.showGutsAt(i,j,k,l)
		print self.Name,"ModelSpec:"
		self.ModelSpec.showGutsAt(i,j,k,l)
		print self.Name,"BaseCounts:"
		self.BaseCounts.showGutsAt(i,j,k,l)
		print self.Name,"BaseOdds:"
		self.BaseOdds.showGutsAt(i,j,k,l)
		print self.Name,"BaseBalance:"
		self.BaseBalance.showGutsAt(i,j,k,l)
		print self.Name,"BaseBalanceBias:"
		self.BaseBalanceBias.showGutsAt(i,j,k,l)

def load(pth, s):
		rc=StageObj()
		rc.Name=s
		rc.FID = gBound.gDNSMFID.parse(join([pth,'/',s],sep=''))
		rc.Topology = gBound.gDNSMatrixAugmented.parse(join([pth,'/',s,'Topology'],sep=''))
		rc.ModelSpec = gBound.gDNSMatrixAugmented.parse(join([pth,'/',s,'ModelSpec'],sep=''))
		rc.BaseCounts = gBound.gDNSMatrixAugmented.parse(join([pth,'/',s,'BaseCounts'],sep=''))
		rc.BaseOdds = gBound.gDNSMatrixAugmented.parse(join([pth,'/',s,'BaseOdds'],sep=''))
		rc.BaseBalance = gBound.gDNSMatrixAugmented.parse(join([pth,'/',s,'BaseBalance'],sep=''))
		rc.BaseBalanceBias = gBound.gDNSMatrixAugmented.parse(join([pth,'/',s,'BaseBalanceBias'],sep=''))
		return rc


