def anagram(strs):
   hash={}
   for char in strs:
      ch="".join(sorted(char))
      if ch not in hash:
         hash[ch]=[]
      hash[ch].append(char)
   return list(hash.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(anagram(strs))
  