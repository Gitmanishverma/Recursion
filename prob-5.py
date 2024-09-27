# Sorting an array using recursion only'
def sorting(arr):

    #Base Condition
    if len(arr) == 1:
        return

    #Induction
    last_num = arr[-1]
    arr.pop()
    sorting(arr)
    insert(arr, last_num)

    return arr

def insert(arr, last_num):

    #Base Condition
    if len(arr) == 0 or arr[-1] <= last_num:
        arr.append(last_num)
        return

    #Induction
    val = arr[-1]
    arr.pop()
    insert(arr, last_num)
    arr.append(val)



arr1=[4,3,5,2,8,0,-1,3,4,6]
print(sorting(arr1))