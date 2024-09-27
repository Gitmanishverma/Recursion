# sum of array elements using recursion
arr=[1,2,3,4,5,6,4] # change the input as your requrement
def sum_arr(arr):
    if len(arr)==1:
        return arr[0]
    else:
        n=len(arr)
        return  arr[n-1]+sum_arr(arr[0:n-1])
    
print('Sum of elements of arr :', sum_arr(arr))