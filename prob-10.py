## find minmum and Maximun element in an arrrY USING RECURSION
arr=[1,3,4,-5,-4,8,3,6]
n=len(arr)

def min_recu(arr,n):
    if n==0:
        return arr[n]
    else:
        return min(arr[n-1],min_recu(arr,n-1))

print("The minimum element in the given array is:", min_recu(arr,n))

## find the maximum element in an array 

def max_recu(arr,n):
    if n==0:
        return arr[n]
    else:
        return max(arr[n-1],max_recu(arr,n-1))
    

print("The maximun element in the given array is:",max_recu(arr,n))