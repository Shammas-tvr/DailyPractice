def freq_char(char):
    count={}
    dup=set()
    for l in char:
        if l not in dup:
            dup.add(l)
            count[l]=1
        else:
            count[l]+=1
    return count

print(freq_char("am going to vadakara"))            