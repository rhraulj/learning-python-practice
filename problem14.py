# Write apython function to print first lines of the following pattern.
# ***
# **
# *

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
    
pattern(3)
