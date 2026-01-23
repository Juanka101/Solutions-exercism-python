"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40 

PREPARATION_TIME = 0


def bake_time_remaining(minutes):
    """
    this function calculate the bake time remaindin  
    """
    result = EXPECTED_BAKE_TIME - minutes
    return result

def preparation_time_in_minutes(number_of_layers):
    """
    this function calculate
    the time take for number of layers 
    this layers take two minutes 
    """
    result = number_of_layers * 2
    return result 



def elapsed_time_in_minutes(number_of_layers, minutes):
    """ this function takes two integers, 
    
    time and number of lasagna for calculate 
    
    total elapsed minutes cooking
    
    the lasagna
    """
    result = minutes + preparation_time_in_minutes(number_of_layers)
    return result
    