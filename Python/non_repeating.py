def non_repeating_char(word):
    count={}
    for char in word:
        if char not in count:
            count[char]=1
        else:
            count[char]+=1
    for char in word:
        if count[char] == 1:
            return char
    return None 


print(non_repeating_char("shammas"))
