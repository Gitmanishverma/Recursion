## FIND THE FACTORIAL OF NUMBER USING RECURSION

def factorail(num):
    if num==1:
        return 1
    elif num==0:
        return 0
    else:
        return num *factorail(num-1)
    
nums=int(input("Enter the number: "))
print("The factorailof a given number is :")
print(factorail(nums))