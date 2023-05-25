from Operation import Operation

class History:

    def __init__(self) -> None:

        self._data = []
        self._displayData = []

    def clear_history(self) -> None:
        self._data.clear()

    def getAllHistory(self,):
        return self._data
    
    '''
    filter history by operation and return it as list
    '''
    def getHistoryByOperation(self, operation:str) -> list:
        print('history data', self._data, operation)
        print('display data',self._displayData)
        self._displayData =  list(filter(lambda op: operation in op.operation, self._data))
        
        # return self._displayData
        return list(map(lambda x: str(x), self._displayData))
    
    '''
    data displays fully. no filter. 
    '''
    def clearSearch(self,):
        self._displayData = self._data
        return self._displayData

    '''
    save object of type Operation to history
    '''
    def saveToHistory(self, calculation:Operation):
        self._data.append(calculation)

    '''
    save operation by specifying operation and result yourself.
    '''
    def saveToHistory(self,operation:str,result:str):

        op = Operation(operation=operation,result=result)    
        self._data.append(op)

    def __str__(self) -> str:
        return "[" + ", ".join(str(item) for item in self._data) + "]"

        