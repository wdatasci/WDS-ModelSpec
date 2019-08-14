/* originally based on the Vertica example TopKPerPartition with params */

#include "Vertica.h"
#include <string>


using namespace Vertica;
using namespace std;

const char __NewName[]="RowIndex";

class lUDTFCore : public TransformFunction
{
	vint BlockMaxLength=10;
	bool EndPointInclusive=false;
	vint BeginAt=0;
	string NewName=__NewName;

	virtual void setup(ServerInterface &srvInterface, const SizedColumnTypes &argTypes)
	{
		ParamReader paramReader = srvInterface.getParamReader();            
		if (paramReader.getNumCols()>0) {
			try { BlockMaxLength = paramReader.getIntRef("BlockMaxLength");} catch(...) { }
			try { EndPointInclusive = paramReader.getBoolRef("EndPointInclusive");} catch(...) { }
			try { BeginAt = paramReader.getIntRef("BeginAt");} catch(...) { }
			try { NewName = paramReader.getStringRef("NewName").str();} catch(...) { }
		}
	}    

	virtual void processPartition(ServerInterface &srvInterface, 
			PartitionReader &inputReader, 
			PartitionWriter &outputWriter)
	{
		try {
			vint row=0;
			vint NRowMax;
			vint offset=0;
			do {
				if (row>0) vt_report_error(0, "Partition by blocks for list_range can have at most 1 row", "");
				NRowMax = inputReader.getIntRef(1);  
				if (inputReader.getNumCols()>2) 
					offset=inputReader.getIntRef(2);
				row++;
			} while (inputReader.next());

			vint i,ii;
			if (EndPointInclusive) NRowMax+=1;
			if (NRowMax>BlockMaxLength) NRowMax=BlockMaxLength;

			for (ii=BeginAt;ii<NRowMax;ii++) {
				outputWriter.copyFromInput(0,inputReader,0);
				outputWriter.setInt(1, offset+ii);
				outputWriter.next();
			}

		} catch(exception& e) {
			// Standard exception. Quit.
			vt_report_error(0, "Exception while processing partition: [%s]", e.what());
		}
	}
};


class lUDTFFactory : public TransformFunctionFactory
{
	virtual void getPrototype(ServerInterface &srvInterface, ColumnTypes &argTypes, ColumnTypes &returnType)
	{
		argTypes.addAny();
		returnType.addAny();
	}

	virtual void getReturnType(ServerInterface &srvInterface, 
			const SizedColumnTypes &inputTypes, 
			SizedColumnTypes &outputTypes)
	{
		string NewName=__NewName;
		ParamReader paramReader = srvInterface.getParamReader();            
		if (paramReader.getNumCols()>0) {
			try { NewName = paramReader.getStringRef("NewName").str();} catch(...) { }
		}

		size_t i=0;
		outputTypes.addArg(inputTypes.getColumnType(i), inputTypes.getColumnName(i));
		i++;
		outputTypes.addArg(inputTypes.getColumnType(i), NewName);
		i++;
	}

	virtual void getParameterType(ServerInterface &srvInterface,
			SizedColumnTypes &parameterTypes)
	{
		parameterTypes.addInt("BlockMaxLength");
		parameterTypes.addBool("EndPointInclusive");
		parameterTypes.addInt("BeginAt");
		parameterTypes.addVarchar(32,"NewName");
	}


	virtual TransformFunction *createTransformFunction(ServerInterface &srvInterface){ 
		return vt_createFuncObject<lUDTFCore>(srvInterface.allocator); 
	}

};

RegisterFactory(lUDTFFactory);
