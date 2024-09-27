# Find the lenght of string using recursion
s="Git Manish Verma" 
# This program will so count spaces 

def lenght(s):
    if s=="":
        return 0
    else:
        return 1+lenght(s[1:])
print(lenght(s))

