def find_missing_nbr_arr(arr):
    n=len(arr)+1
    total = n * (n + 1) // 2
    return total - sum(arr)


print(find_missing_nbr_arr([1,3,4,5]))