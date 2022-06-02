import vertica_sdk



class pyRawBones(vertica_sdk.TransformFunction):

    def __init__(self, srvInterface):
        params=srvInterface.getParamReader()
        if params.containsParameter("InputBlockMaxLength"):
            self.InputBlockMaxLength=srvInterface.getParamReader().getInt("InputBlockMaxLength")
        else:
            self.InputBlockMaxLength=1
        if params.containsParameter("BlockMaxLength"):
            self.BlockMaxLength=srvInterface.getParamReader().getInt("BlockMaxLength")
        else:
            self.BlockMaxLength=1
        if params.containsParameter("EndPointInclusive"):
            self.EndPointInclusive=srvInterface.getParamReader().getBool("EndPointInclusive")
        else:
            self.EndPointInclusive=False

    def processPartition(self,srvInterface, inputReader, outputWriter):
        try: #{

            row=0 
            rowM1=-1
            first_row=0
            last_row=-1

            row_to_output=[]
            row_index_last=[] 
            row_index_next=[] 

            ID=None
                    
            N=None
                    
            Offset=None
                    

            try: #{

                while True:
                
                    if (self.InputBlockMaxLength > 0 and row >= self.InputBlockMaxLength) :
                        raise Exception("Partition by blocks are limited to InputBlockMaxLength rows")

                    if (row==0) :
                        try:
                            ID = inputReader.getInt(0)
                        except Exception as e:
                            ID = None
                        try:
                            N = inputReader.getInt(1)
                        except Exception as e:
                            N = None
                        try:
                            Offset = inputReader.getInt(2)
                        except Exception as e:
                            Offset = None

                        row_index_last.append(None)
                        row_index_next.append(None)

                    else:

                        row_index_next[rowM1]=row
                        row_index_last.append(rowM1)
                        row_index_next.append(None)


                    row_to_output.append(True)
                    row += 1
                    rowM1 +=  1

                    if inputReader.next():
                        continue
                    else:
                        break

            #}
            except Exception as e:
                raise e

            last_row=row

            if N is None:
                N=0

            if Offset is None:
                Offset=0


            if self.EndPointInclusive:
                RowIndex=list(range(Offset, Offset+N+1))
            else:
                RowIndex=list(range(Offset, Offset+N))

            for row, v in enumerate(RowIndex):
                
                try:
                    if ID is None:
                        outputWriter.setNull(0)
                    else:
                        outputWriter.setInt(0, ID)
                except Exception as e:
                    raise e

                try:
                    if RowIndex[row] is None:
                        outputWriter.setNull(1)
                    else:
                        outputWriter.setInt(1, v)
                except Exception as e:
                    raise e
                
                outputWriter.next()
        #}
        except Exception as e:
            raise e


class pyRawBones_Factory(vertica_sdk.TransformFunctionFactory):
    def getParameterType(self, srvInterface, parameterTypes):
        parameterTypes.addInt("InputBlockMaxLength")
        parameterTypes.addInt("BlockMaxLength")
        parameterTypes.addBool("EndPointInclusive")
    def getPrototype(self, srvInterface, argTypes, returnType):
        argTypes.addInt()  # ID
        argTypes.addInt()  # N
        argTypes.addInt()  # Offset
        returnType.addInt()  # ID
        returnType.addInt()  # RowIndex
    def getReturnType(self, srvInterface, inputTypes, outputTypes):
        outputTypes.addInt("ID")
        outputTypes.addInt("RowIndex")
    def createTransformFunction(cls, srvInterface):
        return pyRawBones(srvInterface)

