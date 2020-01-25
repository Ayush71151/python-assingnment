class myerror(Exception):
    def __init__(self,value):
        self.value=value
    def _str_(self):
        return(repr(self.value))
try:
     raise(myerror(3*2))
except myerror as error :
        print("an exception is occur",error.value)
    