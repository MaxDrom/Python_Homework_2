class FunctionCaller:
    def __init__(self, function):
        self.function = function
        self.jobs = []
    
    def append_job(self,  *args, **kwargs):
        self.jobs.append((args, kwargs))
    
    def call(self):
        if len(self.jobs) == 0:
            print("Nothing to do")
            return
        for args, kwargs in self.jobs:
            arguments_str = ", ".join(str(arg) for arg in args)
            arguments_str += "".join(f', {key} = {value}' for key, value in kwargs.items()) + "."
            print("Calling for job", arguments_str, "Result", self.function(*args, **kwargs), sep = " ")
        self.jobs = []

import math
def my_sin(x, coeff = 1):
    return coeff*math.sin(x)

caller  = FunctionCaller(my_sin)
caller.call() 
caller.append_job(0, coeff = 10)
caller.append_job(0.5, coeff = 0)
caller.append_job(1, coeff = 1)
caller.call()
caller.call() 


    
