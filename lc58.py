def lengthOfLastWord( s) :
        i=j=len(s)-1
        if s.isalpha():
            return len(s)
        while s[j]==' ':
            i-=1
            j-=1
        while s[i].isalpha():
            i-=1
        return j-i
s="Hello World"
print(lengthOfLastWord(s))