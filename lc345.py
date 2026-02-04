def revVowel(s):
    left,right=0,len(s)-1
    l=list(s)
    while(left<right):
        if l[left] not in "aeiouAEIOU":
            left+=1
        elif l[right] not in "aeiouAEIOU":
            right-=1
        else:
            temp=l[left]
            l[left]=l[right]
            l[right]=temp
            left+=1
            right-=1
    return "".join(l)
s= "IceCreAm" 
print(revVowel(s))                