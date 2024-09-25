## sum of all the elemnts of an  arrry using recursion


def func_sum(arr,n):
    if n==0:
        return arr[n]
    else:
        return  func_sum(arr,n-1)+arr[n]

arr=[1,2,3,4,5]
n=len(arr)-1
print("The sum of the given array is :",func_sum(arr,n))
