def appendCharacters( s, t) :
        i=j=0
        count=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                j+=1
            i+=1
        if i==len(s):
            count=len(t)-j
        return count 
s="coaching"
t="coding"
print(appendCharacters(s,t))