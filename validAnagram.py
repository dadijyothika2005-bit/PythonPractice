
def isAnagram( s, t):
    s_count={}
    if len(s)!=len(t):
        return False
    for x in s:
       s_count[x]=s_count.get(x,0)+1
    for y in t:
        if y in s_count:
            s_count[y]-=1
    for y in t:
        if y not in s_count or s_count[y]!=0:
         return False        
    return True   
s="racecar"
t="carrace"
print(isAnagram(s,t))