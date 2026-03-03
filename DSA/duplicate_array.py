def find_duplicate(arr):
    visited=set()
    doop=set()
    for num in arr:
        if num in visited:
            doop.add(num)
        else:
            visited.add(num)
    return doop

print(find_duplicate([12,13,12,65,65,45,45,7,9,8]))            
