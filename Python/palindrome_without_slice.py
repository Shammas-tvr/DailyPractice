def palindrome_without_slice(word):
    if len(word) <=1:
        return word
    reversed=""
    left=len(word)-1
    right=0
    while left > right:
        if word[right] != word[left]:
            return False
        left-=1
        right+=1
    return True


print(palindrome_without_slice("malayala"))
