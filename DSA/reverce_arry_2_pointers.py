def reverse_array_two_pointers(arr):
    if len(arr)<=1:
        return arr
    right=0
    left=len(arr)-1
    while right <= left:
        arr[right],arr[left]=arr[left],arr[right]
        right+=1
        left-=1
    return arr

print(reverse_array_two_pointers([1,2,3,4,5]))