## Convert decimal to binary using recursion

def funct_db(nums):
    if nums==01:
        return 0
    else:
        return (nums%2 +10*funct_db(nums//2) )
    
nums=int(input("Enter the number :"))

print("The binary number is :",funct_db(nums))