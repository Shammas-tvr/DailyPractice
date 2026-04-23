def reverse_arry(arr):
    if len(arr) <= 1:
        return arr
    
    right=0
    left=len(arr)-1
    while right < left:
        arr[right],arr[left]=arr[left],arr[right]
        right+=1
        left-=1
    return arr

print(reverse_arry([1,23,6,7,23,34]))    