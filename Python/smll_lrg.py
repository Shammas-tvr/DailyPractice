def find_smaller_larger(arr):
    larg=float('-inf')
    small=float('inf')
    if len(arr) <=1:
        return larg
    for num in arr:
        if num > larg:
            larg = num 
        if num < small:
            small = num 
    return larg,small

print(find_smaller_larger([5, 1, 10]))            
    
    