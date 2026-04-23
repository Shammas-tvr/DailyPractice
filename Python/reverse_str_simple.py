def reverse_str(s):
    if len(s) <= 1:
        return s
    rev_str = ""
    for i in range(len(s)-1, -1, -1):  # fixed here
        rev_str += s[i]
    return rev_str

print(reverse_str("shammas"))