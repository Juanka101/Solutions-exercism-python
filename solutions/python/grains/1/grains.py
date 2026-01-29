"""
Hello everyone, mathematically the operation 
I used can be replaced by dividing the result 
of the enhancement of the box number by 2
in the total function I chose to directly 
throw the result instead of doing an operation 
each time it is executed, but in case you only
want to do the formula of (2 ** 64 ) // 2
"""

def square(number):
    if number > 0 and number <= 64:
        return 2 ** (number -1) 
        #the form (2 ** number) // 2 it also works
    else:
        raise ValueError ("square must be between 1 and 64")
        
def total():
    return 18446744073709551615
