def remove_duplicate(arr):
    dupli=set()
    i=0
    while i < len(arr):
        if arr[i] in dupli:
            arr.pop(i)
        else:
            dupli.add(arr[i])    
            i+=1
    return arr


print(remove_duplicate([1,3,2,1,4,6,9,4,9]))    
