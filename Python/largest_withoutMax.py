def find_largest_without_max(nums):
    larg=0
    for num in nums:
        if larg < num:
            larg=num
    return larg

print(find_largest_without_max([13,56,323,643,77]))        