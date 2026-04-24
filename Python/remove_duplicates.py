def remove_duplicates_preseving(arr):
    uni=set()
    i=0
    while i < len(arr):
        if arr[i] in uni:
            arr.pop(i)
        else:
            uni.add(arr[i])
            i+=1
    return arr

print(remove_duplicates_preseving([5, 2, 5, 7, 2, 9]))            
