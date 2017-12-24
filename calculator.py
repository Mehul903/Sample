"""
@author: MPatel

"""

## Simple class to add given list of numbers:
class calculator:
    
    def __init__(self):        
        pass    
    
    def addition(self, *args):        
        
        total = 0
        for val in args:
            total+=val
        
        return total
