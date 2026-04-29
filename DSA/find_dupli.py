def find_duplicates(arr):
    if len(arr) < 1:
        return "there is no duplciates"
    dup=set()
    seen=set()
    for num in arr:
        if num in seen:
            dup.add(num)
        else:
            seen.add(num)
            
    return   list(dup)


print(find_duplicates([123,3453,634,74,34,34,74]))
