# print 1-N using recursion

def function_print(n):
    if (n==1):
        print(1)
    else:
        function_print(n-1)
        print(n)



n=int(input("Enter the number: "))
(function_print(n))

    
