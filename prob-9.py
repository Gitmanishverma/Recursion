## Find the sum of digits of number using recursion


nums=int(input("Enter the number :"))

def digi_sum(nums):
    if (nums==0):
        return 0
    else:
        return (nums%10 + digi_sum(int(nums/10)))
    
print("The sum of digits is :",digi_sum(nums))


