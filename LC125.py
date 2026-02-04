def isPalindrome(s):
 k=len(s)-1
 for i in range(len(s)//2):
    if(s[k]!=s[i]):
        return False  
    k-=1
 return True     
s="2345432"
print(isPalindrome(s))
    
        