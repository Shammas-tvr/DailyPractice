def second_larg_unique(arr):
    larg=float('-inf')
    sec=float('-inf')
    for num in arr:
        if num > larg:
            sec=larg
            larg=num
        elif num < larg and num > sec:
            sec=num    
    return sec

print(second_larg_unique([123,33,-888,10]))        