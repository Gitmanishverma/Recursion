# Reverse a string using recursion 
s="GITMANISHVERMA"  # take input as per your requirement 
def reverse(str):
    if len(str)==1:
        return str[0]
    

    else:
        n=len(str)
        return (str[n-1]+reverse(str[0:n-1]))


print("The given string is :",s,"\n","Reverse is :",reverse(s))