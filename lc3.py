def lengthOfLongestSubstring( s):
        left=0
        hash_map={}
        max_length=0
        for right in range(len(s)):
             char=s[right]
             hash_map[char]=hash_map.get(char,0)+1
             while(hash_map[char]>1):
                left_char=s[left]
                hash_map[left_char]-=1
                if hash_map[left_char]==0:
                    del hash_map[left_char]   
                left+=1
             current_length=right-left+1   
             max_length=max(max_length,current_length)
        return max_length    
s="abcabcbb"
print(lengthOfLongestSubstring(s))