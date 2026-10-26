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


