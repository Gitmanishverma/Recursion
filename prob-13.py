##  CHECK WETHER THE STRING IS PALINDROM OR NOT?


def ispal(s):
    temp=s
    if len(s)==1:
        return s[0]
    else:
        n=len(s)
        z=(s[n-1]+ispal(s[0:n-1])) 
        print(z)
        return
        
        
s="sad"
print(ispal(s))