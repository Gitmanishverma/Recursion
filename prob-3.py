## find mean of an arr which sum of all the element divided by no. of elements 


def Function_mean(arr,n):
    if n==1:
        return arr[n-1]
    else:
        return ((Function_mean(arr,n-1)*(n-1)+n)/n)
    


arr=[1,2,3,4,5]
n=len(arr)
print("the mean of given arr is: ",Function_mean(arr,n))
