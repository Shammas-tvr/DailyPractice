
def reverse_str(s):
    if len(s)<=1:
        return s
    right=len(s)-1
    left=0
    s=list(s)
    while left <=right:
        s[left],s[right]=s[right],s[left]
        right-=1
        left+=1
    return "".join(s)

print(reverse_str("shammas"))    