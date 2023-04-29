
'''
Objects of this type are saved to history
'''
class Operation():

    '''
    
    Params:
    operation will be string of: + - * / sin() etc
    result either string or float, we need it for display only.
    
    
    '''
    def __init__(self, operation:str, result=None) -> None:
 
        self.operation = operation
        self.result = result


    def __str__(self) -> str:
         return f"Operation({self.operation}, {self.result})"
        
