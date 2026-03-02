def vowels_count(s):
    vowels="AEIOUaeiou"
    count=0
    for i in s:
        if i in vowels:
            count+=1
    return count 


print(vowels_count("anna adam "))


# Better:
# vowels = set("AEIOUaeiou")
# Because:
# set lookup → O(1)
# string lookup → O(n)