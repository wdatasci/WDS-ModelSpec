# SMV3_MainFunctions

import sys
from string import *
from numpy import *
from array import array
from fpformat import *
#import random

from random import Random

#import gBound.gSMFID
#import gBound.gSMStateSpaceSpec
#import gBound.gSMStocksAndFlowsSpec
#import gBound.gSMMatrix
#import gBound.SMMatrixAugmented
#import gBound.SMStageObj
#import gBound.gSMDriverInfo

import ArtificialVariableFunctions 
import OldMatrixFunctions





def PSMFIDOddsFillerWithBase(
		NMFID,
		PFIDInputs, 
		SS, 
		SF, 

		StageObjs,
		StageModelSpecs,
		StageTopologies,
		#StageBaseCounts,
		StageBaseOdds,
		#StageBaseBalance,
		StageBaseBalanceBias,
		StageBaseFlows,

		onlyrow=0, 
		nFlows=0, 
		PFIDInputsIndex=1,
		PFIDInputsIndex2=0,
		NormList=(0, -1),
		nSims=0,
		dSimSeed=None,
		unitDFS=[],
		StructuralUnitVariation=[],

		lastarg=0):
  
	if nSims>0 and len(StructuralUnitVariation)>0:
		SUVInd=1
	else:   SUVInd=0
	
	nStages=int(SS.getStages().getNumber())
	nStates=int(SS.getStates().getNumber())
	# nFlows=int(SF.getFlows().getNumber())
	nFlowsMRN=int(SF.getFlows().getMacroreturnnumber())
	nStocks=int(SF.getStocks().getNumber())
	
	#nInputs=int(PFIDInputs.SMMatrixGuts.shape[1])-2
	nInputs=int(PFIDInputs.SMMatrix.getNumberofstates())-2
	#rint "nInputs=",nInputs

	nBetas=int(StageObjs[NMFID][0].FID.getBetas().getNumber())
	rc=zeros((nStates,nStates),double)

	if nFlows > 0:
		vrc=[rc.copy() for i in range(nFlows+2)]
	else:
		vrc=[rc]

	for i in range(nBetas):

		u=int(StageObjs[NMFID][0].FID.getBetas().getBeta()[i].getI())

		if u==0: iia=0; iib=nStates
		else: iia=u-1; iib=u

		if onlyrow==0 or u==onlyrow:
			if onlyrow>0: u=1;iia=0;iib=1
			v=int(StageObjs[NMFID][0].FID.getBetas().getBeta()[i].getJ())
			fi=int(StageObjs[NMFID][0].FID.getBetas().getBeta()[i].getFlowref())
			tempdouble=StageObjs[NMFID][0].FID.getBetas().getBeta()[i].getValue()
			if v==0: 
				for ii in range(iia,iib): 
					for jj in range(nStates):
						if ii<>jj: vrc[fi][ii,jj] += tempdouble
			else:
				v-=1
				for ii in range(iia,iib): 
					vrc[fi][ii,v] += tempdouble
		
	BaseOffsets=zeros(nFlows+2)

	for i in range(int(StageObjs[NMFID][0].FID.getFunctionalinputs().getNumber())):
		#rint "i in FunctionalInputs=", i
		if i<nInputs:

			x=float(PFIDInputs.SMMatrixGuts[0,i+2,PFIDInputsIndex,PFIDInputsIndex2,0,0])

			if int(StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getBasesetind()) == 1:
				#rint "caught BaseSetInd ", i, x
				BaseOffsets[int(StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getFlowref())]=int(x)
			elif StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getBasesetind() == -1:
				NullIN=PDFInputs[i,0]
			else:
				u=int(StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getI())

				if u==0: iia=0; iib=nStates
				else: iia=u-1; iib=u

				if onlyrow==0 or u==onlyrow:
					if onlyrow>0: u=1;iia=1;iib=1
					v=int(StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getJ())
					fi=int(StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getFlowref())
					si=int(StageObjs[NMFID][0].FID.getFunctionalinputs().getFunctioninput()[i].getOpzeroorone())
					if (nFlows==0 and fi==0) or (nFlows>0 and fi<=nFlows):
						if v==0: 
							if si == 0:
								for ii in range(iia,iib): 
									for jj in range(nStates):
										vrc[fi][ii,jj] += x
							else:
								for ii in range(iia,iib): 
									for jj in range(nStates):
										vrc[fi][ii,jj] *= x
						else:
							v-=1
							if si == 0:
								for ii in range(iia,iib): 
									vrc[fi][ii,v] += x
							else:
								for ii in range(iia,iib): 
									vrc[fi][ii,v] *= x
					
		

	for i in range(int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getNumber())):

		iii=int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getFunctioninput()[i].getInputreference())-1
		#rint "i,iii in FunctionalInputs=", i, iii

		if iii<nInputs:
			x=float(PFIDInputs.SMMatrixGuts[0,iii+2,PFIDInputsIndex,PFIDInputsIndex2,0,0])

			if int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getFunctioninput()[i].getBasesetind()) == -1:
				NULLIN=PDFInputs[i,0]
			else:
				u=int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getFunctioninput()[i].getI())

				if u==0: iia=0; iib=nStates
				else: iia=u-1; iib=u

				if onlyrow==0 or u==onlyrow:
					if onlyrow>0: u=1;iia=1;iib=1
					v=int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getFunctioninput()[i].getJ())
					fi=int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getFunctioninput()[i].getFlowref())
					si=int(StageObjs[NMFID][0].FID.getRedundantfunctionalinputs().getFunctioninput()[i].getOpzeroorone())
					if (nFlows==0 and fi==0) or (nFlows>0 and fi<=nFlows):
						if v==0: 
							if si == 0:
								for ii in range(iia,iib): 
									for jj in range(nStates):
										vrc[fi][ii,jj] += x
							else:
								for ii in range(iia,iib): 
									for jj in range(nStates):
										vrc[fi][ii,jj] *= x
						else:
							v-=1
							if si == 0:
								for ii in range(iia,iib): 
									vrc[fi][ii,v] += x
							else:
								for ii in range(iia,iib): 
									vrc[fi][ii,v] *= x
					


	nflowstemp=2
	if nFlows > 0:
		nflowstemp=nFlows+2
	else:
		nflowstemp=1

	if nSims>0:
		for i in range(nStates):
			u=i
			if onlyrow==0 or u==onlyrow:
				if onlyrow>0: u=0
				for j in range(nStates):
					if StageTopologies[NMFID][0].SMMatrixGuts[i,j,0,0,0,0] > 0:
						k=0
						vrc[k][u,j]=exp(mnmx(10.0,-10.0,vrc[k][u,j]))
						if StageBaseOdds[NMFID][0].SMMatrixGuts[i,j,BaseOffsets[0],0,0,0]>0.0:
							vrc[k][u,j]*=StageBaseOdds[NMFID][0].SMMatrixGuts[i,j,BaseOffsets[0],0,0,0]
						elif i<>j:
							vrc[k][u,j]=0.0000001
						if SUVInd==1: vrc[k][u,j]*=StructuralUnitVariation[u,j]
					else:
						vrc[k][u,j]=0.0

		if int(SF.getUnits().getUnit()[0].getTosimind())==1 and SF.getUnits().getUnit()[0].getSimcvperperiod()>0:
			dBiasCV=SF.getUnits().getUnit()[0].getSimcvperperiod()
			dBiasSigma2=log(1+dBiasCV*dBiasCV)
			dBiasSigma=sqrt(dBiasSigma2)
			dBiasMu=-dBiasSigma2/2
			r=Random()
			for i in range(nStates):
				for j in range(nStates):
					if i <> j and StageTopologies[NMFID][0].SMMatrixGuts[i,j,0,0,0,0] > 0:
						vrc[0][i,j]*=r.lognormvariate(mu=dBiasMu,sigma=dBiasSigma)

		vrc[0]=RAGMatrixFunctions.RowNormIt(vrc[0],nStates,nStates)
		#rint "nSims:=", nSims
		if dSimSeed==None: dSimSeed=random.seed()
		for i in range(nStates):
			lnSim=int(unitDFS[i]+.0000001)
			#rint "lnSims[i],unitDFS[i]:=", i, lnSim, unitDFS[i]
			if abs(float(lnSim)-unitDFS[i])>.1: sys.exit(0)
			if lnSim<=0:
				for j in range(nStates): vrc[0][i,j]=0.0
			else:
				for j in range(1,nStates):
					vrc[0][i,j]+=vrc[0][i,j-1]
					#rint "vrc[0][i,j]=",i,j,vrc[0][i,j]
				if abs(vrc[0][i,-1])>.0000001:
					vrc[0][i,-1]=1.0
					tmpsim=random.rand(lnSim)
					tmpsim.sort(kind='quicksort')
					#or j in range(lnSim):
						#rint "tmpsim[j]=",j,tmpsim[j]
					j=0
					for k in range(nStates):
						while j<lnSim and tmpsim[j]<vrc[0][i,k]: j+=1
						vrc[0][i,k]=float(j)
						#rint "vrc[0][i,k]=",i,k,vrc[0][i,k]
					for j in range(nStates-1,0,-1):
						vrc[0][i,j]-=vrc[0][i,j-1]

					if vrc[0][i,i]>0:
						for j in range(nStates): 
							if i<>j: vrc[0][i,j]/=vrc[0][i,i]
						vrc[0][i,i]=1.0
					#else:
						#vrc[0][i,i]=.0000001
				#or j in range(nStates):
					#rint "vrc[0][i,j]=",i,j,vrc[0][i,j]
				#f i==1: sys.exit(0)

	kstart=0
	if nSims>0:kstart=1

	for i in range(nStates):
		u=i
		if onlyrow==0 or u==onlyrow:
			if onlyrow>0: u=0
			for j in range(nStates):
				if StageTopologies[NMFID][0].SMMatrixGuts[i,j,0,0,0,0] > 0:
					for k in range(kstart,nflowstemp):
						if k==0:
							vrc[k][u,j]=exp(mnmx(10.0,-10.0,vrc[k][u,j]))
							if StageBaseOdds[NMFID][0].SMMatrixGuts[i,j,BaseOffsets[0],0,0,0]>0.0:
								vrc[k][u,j]*=StageBaseOdds[NMFID][0].SMMatrixGuts[i,j,BaseOffsets[0],0,0,0]
							elif i<>j:
								vrc[k][u,j]=0.0000001
						elif k==nFlows+1:
							vrc[k][u,j]=vrc[0][u,j]*exp(mnmx(10.0,-10.0,vrc[k][u,j]))
							if StageBaseBalanceBias[NMFID][0].SMMatrixGuts[i,j,BaseOffsets[0],0,0,0]<>0.0 and i<>j:
								vrc[k][u,j]*=exp(mnmx(10.0,-10.0,
									StageBaseBalanceBias[NMFID][0].SMMatrixGuts[i,j,BaseOffsets[k],0,0,0]))
							elif i<>j:
								if nSims>0:
									vrc[k][u,j]=0.0
								else:
									vrc[k][u,j]=0.0000001
						else:
							if vrc[k][u,j] <> 0.0:
								#rint "k,u,j=",k,u,j
								vrc[k][u,j] = exp(min(10.0,max(-10.0,
									vrc[k][u,j]))) * StageBaseFlows[NMFID][k-1][0].SMMatrixGuts[i,j,BaseOffsets[k],0,0,0]
							else:
								vrc[k][u,j] = StageBaseFlows[NMFID][k-1][0].SMMatrixGuts[i,j,BaseOffsets[k],0,0,0]
				else:
					for k in range(nflowstemp):
						vrc[k][u,j]=0.0
	
	if nSims>0:
		if int(SF.getStocks().getStock()[0].getTosimind())==1:
			dBiasCV=SF.getStocks().getStock()[0].getSimcv()
			dBiasSigma2=log(1+dBiasCV*dBiasCV)
			dBiasSigma=sqrt(dBiasSigma2)
			dBiasMu=-dBiasSigma2/2
			r=Random()
			for i in range(nStates):
				for j in range(nStates):
					if i <> j and vrc[-1][i,j]<>0.0:
						vrc[-1][i,j]*=r.lognormvariate(dBiasMu,dBiasSigma)
		for k in range(1,nflowstemp-1):
			if int(SF.getFlows().getFlow()[k-1].getTosimind())==1:
				dBiasCV=SF.getFlows().getFlow()[0].getSimcv()
				dBiasSigma2=log(1+dBiasCV*dBiasCV)
				dBiasSigma=sqrt(dBiasSigma2)
				dBiasMu=-dBiasSigma2/2
				r=Random()
				for i in range(nStates):
					for j in range(nStates):
						if i <> j and vrc[k][i,j]<>0.0:
							vrc[k][i,j]*=r.lognormvariate(dBiasMu,dBiasSigma)

	for k in NormList:
		vrc[k]=RAGMatrixFunctions.RowNormIt(vrc[k],nStates,nStates)

	#for i in range(10):
		#for j in range(10):
			#rint "           vrc[0][u,j]=",i,j,vrc[0][i,j]

	return vrc




def PMultBySMFIDWithCFSubV3(
		units,
		stocks,
		flows,
		StageInputs,
		SS, 
		SF, 

		StageObjs,
		StageModelSpecs,
		StageTopologies,
		#StageBaseCounts,
		StageBaseOdds,
		#StageBaseBalance,
		StageBaseBalanceBias,
		StageFlows,

		nCurrentPrimIndex=0,
		PickUpOnlyPrevStage=False,
		CalledByFunction=True,
		OnlyStage1=True,
		nSims=0,
		StructuralUnitVariation=[],
		SimSeed=None,
		lastarg=1):
  

	nStages=int(SS.getStages().getNumber())
	nStates=int(SS.getStates().getNumber())
	nFlows=int(SF.getFlows().getNumber())
	nFlowsMRN=int(SF.getFlows().getMacroreturnnumber())
	nStocks=int(SF.getStocks().getNumber())
	nStocksMRN=int(SF.getStocks().getMacroreturnnumber())

	nHorizon=int(StageInputs[0][0].SMMatrix.getAdditionalaxesupperlimits().getAxis1())-1
	nHorizon-=int(StageInputs[0][0].SMMatrix.getAdditionalaxeslowerlimits().getAxis1())
	#nInputs=int(StageInputs[0][0].SMMatrixGuts.shape[1])-2

	rc=zeros((nHorizon,(nStocks+nFlows+1)*nStates), double)

	PUFCT=zeros((nStages,nStages,nStates))
	for i in range(nStages):
		for j in range(nStages):
			for k in range(nStates):
				if i==j: PUFCT[i,j,k]=1


	for i in range(int(SS.getBridges().getNumber())):
		if ss.getBridges().getBridge()[i].getType=="PickUp":
			PUFCT[
				SS.getBridges().getBridge()[i].getFrom(),
				SS.getBridges().getBridge()[i].getTo(),
				SS.getBridges().getBridge()[i].getStateposition()
			]=1

	zarg1=zeros(nStates,double)
	arg1=zarg1.copy()
	uarg=[[zarg1.copy() for i in range(nStages)] for j in range(2)]
	sarg=[[[zarg1.copy() for k in range(nStocks)] for i in range(nStages)] for j in range(2)]
	farg=[[[zarg1.copy() for k in range(nFlows)] for i in range(nStages)] for j in range(2)]


	for k in range(nStates):
		uarg[0][0][k]=units[0,0,k]
		for j in range(nStocksMRN):
			sarg[0][0][j][k]=stocks[0,j,0,k]
				

	#wfpayments = zarg.copy()
	wfpayments = zarg1.copy()
	wfpaymentsreduced = 0
	#wfrtb = zarg.copy()
	wfrtb = zarg1.copy()
	wfrtbreduced = 0
	
	one = 1
	two = 0

	Stages=SS.getStages().getStage()
	Stocks=SF.getStocks().getStock()
	Flows=SF.getFlows().getFlow()

	Orders=SF.getOrders().getOrder()


	firstrun=True
	runtake=True

	for indexii in range(nHorizon):

		if two==0:
			one=0
			two=1
		else:
			one=1
			two=0
		
		for indexs in range(nStages):


			#wfpayments=zarg.copy()
			wfpayments=zarg1.copy()

			s=Stages[indexs]

			nInputs=int(StageObjs[indexs][0].FID.getFunctionalinputs().getNumber())
			#tmpmoutarg=zarg.copy()
			#tmpinarg=zarg.copy()
			tmpmoutarg=zarg1.copy()
			tmpinarg=zarg1.copy()
			m2=nStates
			n2=m2

			InputsLag1=zeros(40,double)

			runtake=False
			if firstrun or (nStages>1): runtake=True

			if runtake == False:
				for i in range(nInputs):
					if InputsLag1[i] <> StageInputs[indexs][0].SMMatrixGuts[0,i+2,indexii,nCurrentPrimIndex,0,0]:
						runtake=True
						break
	

			tmpinarg = zarg1.copy()

			for i in range(nStates):
				for j in range(nStages):
					if PUFCT[j,indexs,i]:
						tmpinarg[i]+=uarg[one][j][i]
	
			if indexs==0:
				if StageObjs[indexs][0].FID.getFunctionalinputs().getFunctioninput()[0].getBasesetind() == -1:
					tmpinarg[0]+=rInputVector[indexii,i]
				
			unitDistForSim=[0.00 for i in range(nStates)]
			# balDistForSim=[0.00 for i in range(nStates)]
			for i in range(nStates):
				unitDistForSim[i]=tmpinarg[i]
				# balDistForSim[i]=sarg[one][0][i]


			if (runtake == True) or (nSims>0):
				firstrun=False
				for i in range(nInputs):
					InputsLag1[i]=StageInputs[indexs][0].SMMatrixGuts[0,i+2,indexii,nCurrentPrimIndex,0,0]

				om=PSMFIDOddsFillerWithBase(
					indexs,
					StageInputs[indexs][0],
					SS,SF, 
					StageObjs,
					StageModelSpecs,
					StageTopologies,
					#StageBaseCounts,
					StageBaseOdds,
					#StageBaseBalance,
					StageBaseBalanceBias,
					StageFlows,
					nFlows=nFlowsMRN,
					PFIDInputsIndex=indexii+1,  # this is necessary since the inputs start index at 0
					PFIDInputsIndex2=nCurrentPrimIndex,
					NormList=(0, -1),
					nSims=nSims,
					dSimSeed=SimSeed
					,unitDFS=unitDistForSim
					,StructuralUnitVariation=StructuralUnitVariation
					)
				omu=om[0]
				omub=om[-1]
					


			uarg[two][indexs]=zarg1.copy()
			

			for j in range(nStates):
				for k in range(nStates):
					if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0]>0.0:
						uarg[two][indexs][j]+=tmpinarg[k]*omu[k,j]


			#rint "uarg[one][0]="
			#rint uarg[one][indexs]
			#rint "sarg[one][0][0]="
			#rint sarg[one][indexs][0]

			#rint "sarg[one][0][1]="
			#rint sarg[one][indexs][1]

			#rint "sarg[one][0][2]="
			#rint sarg[one][indexs][2]

			#rint "sarg[one][0][3]="
			#rint sarg[one][indexs][3]


			#sarg2=zarg.copy()
			#farg2=zarg.copy()
			sarg2=zarg1.copy()
			farg2=zarg1.copy()

			for l in range(1,nStocks+nFlows+1):
				
				#tmparg=zarg.copy()
				#tmpinsarg=zarg.copy()
				tmparg=zarg1.copy()
				tmpinsarg=zarg1.copy()

				m=int(Orders[l].getUsf())
				n=int(Orders[l].getIndexorcode())

				#rint "m,n=",m,n

				if m==2:

					n-=1
					
					FRollWeighting=Flows[n].getRollweighting()

					# if n==5:
						# print "FRollWeighting=", FRollWeighting
						# print "prior  tmpinsarg="
						# print tmpinsarg


				
					if valuein(FRollWeighting,
						"BalanceBasisUnitRoll",
						"BalanceBasisUnitRollBounded",
						"BalanceBasisBalanceBiasedRoll",
						"BalanceBasisBalanceBiasedRollBounded",
						"SumOfBases"):
	
						FPrePost=Flows[n].getPrepost()
						if FPrePost=="Pre":
							for i in range(nStates):
								for j in range(nStages):
									if PUFCT[j,indexs,i]:
										if int(Flows[n].getBase1type())==1:
											tmpinsarg[i]+=sarg[one][j][int(Flows[n].getBase1indexorcode())-1][i]* float(Flows[n].getBase1weighting())
										if int(Flows[n].getBase2type())==1:
											tmpinsarg[i]+=sarg[one][j][int(Flows[n].getBase2indexorcode())-1][i]* float(Flows[n].getBase2weighting())
										if int(Flows[n].getBase3type())==1:
											tmpinsarg[i]+=sarg[one][j][int(Flows[n].getBase3indexorcode())-1][i]* float(Flows[n].getBase3weighting())
										if int(Flows[n].getBase4type())==1:
											tmpinsarg[i]+=sarg[one][j][int(Flows[n].getBase4indexorcode())-1][i]* float(Flows[n].getBase4weighting())
										if int(Flows[n].getBase5type())==1:
											tmpinsarg[i]+=sarg[one][j][int(Flows[n].getBase5indexorcode())-1][i]* float(Flows[n].getBase5weighting())
										if int(Flows[n].getBase6type())==1:
											tmpinsarg[i]+=sarg[one][j][int(Flows[n].getBase6indexorcode())-1][i]* float(Flows[n].getBase6weighting())

						elif FPrePost=="Post":
							for i in range(nStates):
								for j in range(nStages):
									if PUFCT[j,indexs,i]:
										if int(Flows[n].getBase1type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase1indexorcode())-1][i]* float(Flows[n].getBase1weighting())
										if int(Flows[n].getBase1type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase1indexorcode())-1][i]* float(Flows[n].getBase1weighting())

										if int(Flows[n].getBase2type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase2indexorcode())-1][i]* float(Flows[n].getBase2weighting())
										if int(Flows[n].getBase2type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase2indexorcode())-1][i]* float(Flows[n].getBase2weighting())

										if int(Flows[n].getBase3type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase3indexorcode())-1][i]* float(Flows[n].getBase3weighting())
										if int(Flows[n].getBase3type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase3indexorcode())-1][i]* float(Flows[n].getBase3weighting())

										if int(Flows[n].getBase4type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase4indexorcode())-1][i]* float(Flows[n].getBase4weighting())
										if int(Flows[n].getBase4type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase4indexorcode())-1][i]* float(Flows[n].getBase4weighting())

										if int(Flows[n].getBase5type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase5indexorcode())-1][i]* float(Flows[n].getBase5weighting())
										if int(Flows[n].getBase5type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase5indexorcode())-1][i]* float(Flows[n].getBase5weighting())

										if int(Flows[n].getBase6type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase6indexorcode())-1][i]* float(Flows[n].getBase6weighting())
										if int(Flows[n].getBase6type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase6indexorcode())-1][i]* float(Flows[n].getBase6weighting())

					elif valuein(FRollWeighting,
						"WaterFallPaydown"):
	
						FPrePost=Flows[n].getPrepost()
						if FPrePost=="Post":
							for i in range(nStates):
								for j in range(nStages):
									if PUFCT[j,indexs,i]:
										if int(Flows[n].getBase1type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase1indexorcode())-1][i]* float(Flows[n].getBase1weighting())
										if int(Flows[n].getBase1type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase1indexorcode())-1][i]* float(Flows[n].getBase1weighting())

										if int(Flows[n].getBase2type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase2indexorcode())-1][i]* float(Flows[n].getBase2weighting())
										if int(Flows[n].getBase2type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase2indexorcode())-1][i]* float(Flows[n].getBase2weighting())

										if int(Flows[n].getBase3type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase3indexorcode())-1][i]* float(Flows[n].getBase3weighting())
										if int(Flows[n].getBase3type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase3indexorcode())-1][i]* float(Flows[n].getBase3weighting())

										if int(Flows[n].getBase4type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase4indexorcode())-1][i]* float(Flows[n].getBase4weighting())
										if int(Flows[n].getBase4type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase4indexorcode())-1][i]* float(Flows[n].getBase4weighting())

										if int(Flows[n].getBase5type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase5indexorcode())-1][i]* float(Flows[n].getBase5weighting())
										if int(Flows[n].getBase5type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase5indexorcode())-1][i]* float(Flows[n].getBase5weighting())

										if int(Flows[n].getBase6type())==1:
											tmpinsarg[i]+=sarg[two][j][int(Flows[n].getBase6indexorcode())-1][i]* float(Flows[n].getBase6weighting())
										if int(Flows[n].getBase6type())==2:
											tmpinsarg[i]+=farg[two][j][int(Flows[n].getBase6indexorcode())-1][i]* float(Flows[n].getBase6weighting())


					#n+=1


					# if n==5:
						# print "post  tmpinsarg="
						# print tmpinsarg


					#rint "tmpinsarg="
					#rint tmpinsarg


					#rint "om[n+1]="
					#or j in range(n2):
						#or k in range(n2):
							#rint "om[n+1][k,j]=",n,k,j,om[n+1][k,j]

				
					#sys.exit(0)



					if FRollWeighting=="UnitBasisUnitRoll":
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinarg[k]*omu[k,j]*om[n+1][k,j]

					elif FRollWeighting=="UnitBasisUnitRollBounded":
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinarg[k]*omu[k,j]*om[n+1][k,j]
						for k in range(n2):
							if wfrtb[k]<0.0: wfrtb[k]=0.0
							if tmparg[k]>wfrtb[k]: tmparg[k]=wfrtb[k]
							wfrtb[k]=wfrtb[k]-tmparg[k]
							if wfrtb[k]<0.0: wfrtb[k]=0.0

					elif FRollWeighting=="UnitBasisBalanceBiasedRoll":
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinarg[k]*omub[k,j]*om[n+1][k,j]

					elif FRollWeighting=="UnitBasisBalanceBiasedRollBounded":
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinarg[k]*omub[k,j]*om[n+1][k,j]
						for k in range(n2):
							if wfrtb[k]<0.0: wfrtb[k]=0.0
							if tmparg[k]>wfrtb[k]: tmparg[k]=wfrtb[k]
							wfrtb[k]=wfrtb[k]-tmparg[k]
							if wfrtb[k]<0.0: wfrtb[k]=0.0

					elif FRollWeighting=="BalanceBasisUnitRoll":
						# if n==5:
							# for j in range(n2):
								# for k in range(n2):
									# print "omu[k,j]=",k,j,omu[k,j]
									# print "omu[n+1]][k,j]=",n,k,j,om[n+1][k,j]
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinsarg[k]*omu[k,j]*om[n+1][k,j]

					elif FRollWeighting=="BalanceBasisUnitRollBounded":
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinsarg[k]*omu[k,j]*om[n+1][k,j]
						for k in range(n2):
							if wfrtb[k]<0.0: wfrtb[k]=0.0
							if tmparg[k]>wfrtb[k]: tmparg[k]=wfrtb[k]
							wfrtb[k]=wfrtb[k]-tmparg[k]
							if wfrtb[k]<0.0: wfrtb[k]=0.0

					elif FRollWeighting=="BalanceBasisBalanceBiasedRoll":
						for j in range(n2):
							for k in range(n2):
								#rint "k,j=",k,j
								#rint StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0]
								#rint tmpinsarg[k]
								#rint tmparg[j]
								#rint omub[k,j]
								#rint om[n+1][k,j]
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinsarg[k]*omub[k,j]*om[n+1][k,j]
								#rint "post,tmparg[j]=",tmparg[j]

					elif FRollWeighting=="BalanceBasisBalanceBiasedRollBounded":
						for j in range(n2):
							for k in range(n2):
								if StageTopologies[indexs][0].SMMatrixGuts[k,j,0,0,0,0] > 0:
									tmparg[j]+=tmpinsarg[k]*omub[k,j]*om[n+1][k,j]
						for k in range(n2):
							if wfrtb[k]<0.0: wfrtb[k]=0.0
							if tmparg[k]>wfrtb[k]: tmparg[k]=wfrtb[k]
							wfrtb[k]=wfrtb[k]-tmparg[k]
							if wfrtb[k]<0.0: wfrtb[k]=0.0

					elif FRollWeighting=="SumOfBases":
						tmparg=tmpinsarg.copy()

					elif FRollWeighting=="WaterFallPaydown":
						tmparg=tmpinsarg.copy()
						for k in range(n2):
							if tmparg[k]<0.0:tmparg[k]=0.0
							if wfpayments[k] > 0.0:
								if tmparg[k] > wfpayments[k]:
									tmparg[k]=wfpayments[k]
									wfpayments[k]=0.0
								else:
									wfpayments[k]=wfpayments[k] - tmparg[k]
							else:
								tmparg[k]=0.0
	
					#n-=1

					if Flows[n].getAors()=="S":
						for k in range(n2):
							wfpayments[k]+=tmparg[k]

					

					# if n==5:
						# print "post  tmparg="
						# print tmparg
						# sys.exit(0)

					#rint "tmparg="
					#rint tmparg

					farg[two][indexs][n]=tmparg.copy()


				elif m==1:

					n-=1

					STreatment=Stocks[n].getTreatment()
					if STreatment=="UR": lomub=omu.copy()
					elif STreatment=="BUR": lomub=omub.copy()
					else: lomub=omub.copy()

					SType=Stocks[n].getType()

					if valuein(SType,"Agg","SumOfBases"):
						for i in range(nStates):
							for j in range(nStages):
								if PUFCT[j,indexs,i]:
									if int(Stocks[n].getBase1type())==1: tmpinsarg[i]+=sarg[two][j][int(Stocks[n].getBase1indexorcode())-1][i]* float(Stocks[n].getBase1weighting())
									if int(Stocks[n].getBase1type())==2: tmpinsarg[i]+=farg[two][j][int(Stocks[n].getBase1indexorcode())-1][i]* float(Stocks[n].getBase1weighting())

									if int(Stocks[n].getBase2type())==1: tmpinsarg[i]+=sarg[two][j][int(Stocks[n].getBase2indexorcode())-1][i]* float(Stocks[n].getBase2weighting())
									if int(Stocks[n].getBase2type())==2: tmpinsarg[i]+=farg[two][j][int(Stocks[n].getBase2indexorcode())-1][i]* float(Stocks[n].getBase2weighting())

									if int(Stocks[n].getBase3type())==1: tmpinsarg[i]+=sarg[two][j][int(Stocks[n].getBase3indexorcode())-1][i]* float(Stocks[n].getBase3weighting())
									if int(Stocks[n].getBase3type())==2: tmpinsarg[i]+=farg[two][j][int(Stocks[n].getBase3indexorcode())-1][i]* float(Stocks[n].getBase3weighting())

									if int(Stocks[n].getBase4type())==1: tmpinsarg[i]+=sarg[two][j][int(Stocks[n].getBase4indexorcode())-1][i]* float(Stocks[n].getBase4weighting())
									if int(Stocks[n].getBase4type())==2: tmpinsarg[i]+=farg[two][j][int(Stocks[n].getBase4indexorcode())-1][i]* float(Stocks[n].getBase4weighting())

									if int(Stocks[n].getBase5type())==1: tmpinsarg[i]+=sarg[two][j][int(Stocks[n].getBase5indexorcode())-1][i]* float(Stocks[n].getBase5weighting())
									if int(Stocks[n].getBase5type())==2: tmpinsarg[i]+=farg[two][j][int(Stocks[n].getBase5indexorcode())-1][i]* float(Stocks[n].getBase5weighting())

									if int(Stocks[n].getBase6type())==1: tmpinsarg[i]+=sarg[two][j][int(Stocks[n].getBase6indexorcode())-1][i]* float(Stocks[n].getBase6weighting())
									if int(Stocks[n].getBase6type())==2: tmpinsarg[i]+=farg[two][j][int(Stocks[n].getBase6indexorcode())-1][i]* float(Stocks[n].getBase6weighting())


					elif valuein(SType,"SLR","Resid"):
						for i in range(nStates):
							for j in range(nStages):
								if PUFCT[j,indexs,i]:
									if int(Stocks[n].getBase1type())==1: tmpinsarg[i]+=sarg[one][j][int(Stocks[n].getBase1indexorcode())-1][i]* float(Stocks[n].getBase1weighting())
									if int(Stocks[n].getBase2type())==1: tmpinsarg[i]+=sarg[one][j][int(Stocks[n].getBase2indexorcode())-1][i]* float(Stocks[n].getBase2weighting())
									if int(Stocks[n].getBase3type())==1: tmpinsarg[i]+=sarg[one][j][int(Stocks[n].getBase3indexorcode())-1][i]* float(Stocks[n].getBase3weighting())
									if int(Stocks[n].getBase4type())==1: tmpinsarg[i]+=sarg[one][j][int(Stocks[n].getBase4indexorcode())-1][i]* float(Stocks[n].getBase4weighting())
									if int(Stocks[n].getBase5type())==1: tmpinsarg[i]+=sarg[one][j][int(Stocks[n].getBase5indexorcode())-1][i]* float(Stocks[n].getBase5weighting())
									if int(Stocks[n].getBase6type())==1: tmpinsarg[i]+=sarg[one][j][int(Stocks[n].getBase6indexorcode())-1][i]* float(Stocks[n].getBase6weighting())

					if valuein(SType,"Agg","SumOfBases","ScaledSum"):
						tmparg=tmpinsarg.copy()

					elif valuein(SType,"SLR"):
						for k in range(n2):
							for j in range(n2):
								tmparg[j]+=tmpinsarg[k]*lomub[k,j]
						for i in range(nStates):
							if int(Stocks[n].getBase1type())==2: tmparg[i]+=farg[two][indexs][int(Stocks[n].getBase1indexorcode())-1][i]* float(Stocks[n].getBase1weighting())
							if int(Stocks[n].getBase2type())==2: tmparg[i]+=farg[two][indexs][int(Stocks[n].getBase2indexorcode())-1][i]* float(Stocks[n].getBase2weighting())
							if int(Stocks[n].getBase3type())==2: tmparg[i]+=farg[two][indexs][int(Stocks[n].getBase3indexorcode())-1][i]* float(Stocks[n].getBase3weighting())
							if int(Stocks[n].getBase4type())==2: tmparg[i]+=farg[two][indexs][int(Stocks[n].getBase4indexorcode())-1][i]* float(Stocks[n].getBase4weighting())
							if int(Stocks[n].getBase5type())==2: tmparg[i]+=farg[two][indexs][int(Stocks[n].getBase5indexorcode())-1][i]* float(Stocks[n].getBase5weighting())
							if int(Stocks[n].getBase6type())==2: tmparg[i]+=farg[two][indexs][int(Stocks[n].getBase6indexorcode())-1][i]* float(Stocks[n].getBase6weighting())

					elif valuein(SType,"Resid"):
						tmparg=wfpayments.copy()


					if Stocks[n].getLateruse()=="Bounder":
						wfrtb=tmparg.copy()

					sarg[two][indexs][n]=tmparg.copy()


		for indexs in range(nStages):
			for j in range(nStates):
				rc[indexii,j]=uarg[two][indexs][j]
				for k in range(nStocks):
					rc[indexii,(k+1)*nStates+j]=sarg[two][indexs][k][j]
				for k in range(nFlows):
					rc[indexii,(k+nStocks+1)*nStates+j]=farg[two][indexs][k][j]

	return rc


def mnmx(arg1,arg2,arg3):
	return min(arg1,max(arg2,arg3))

def valuein(arg1,*args):
	for i in args:
		if arg1==i:
			return True
	return False





