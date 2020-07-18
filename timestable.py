"""
Given an integer n, write a python function which returns a times table grid for all the integers between 1 and n.
The grid should be separated by tabs and new lines.
"""
def number():
    nu = int(input("Times table to: "))
    nu=nu+1
    return nu

def grid():
    nu=number()
    for x in range (1, nu):
        for y in range (1, nu):
            print (x*y, end='\t') 
        print()

grid()
