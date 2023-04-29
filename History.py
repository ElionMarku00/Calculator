from Operation import Operation

class History:

    def __init__(self) -> None:

        self._data = []

    def clear_history(self) -> None:
        self._data.clear()

    def getAllHistory(self,):
        return self._data
    
    '''
    filter history by operation and return it as list
    '''
    def getHistoryByOperation(self, operation:str) -> list:
        return list(filter(lambda op: op.operation.contains(operation),self._data))
    
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



        

    