"""
Given an integer n, write a python function which returns a times table grid for all the integers between 1 and n.
The grid should be separated by tabs and new lines.
"""
def grid(nu):
    nu=nu+1
    output = ""
    for x in range (1, nu):
        for y in range (1, nu):
            output += str(x*y) + '\t' 
        output += "\n"
    
    return output


nu = int(input("Times table to: "))
print(grid(nu))
