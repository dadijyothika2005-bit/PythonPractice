def longestConsecutive(nums):
    y=set(nums)
    x=sorted(y)
    ind=set()
    re=1
    curr=0
    if len(nums)==0:
        return 0
    for i in range(len(x)):
        if x[i]-1 not in y:
            ind.add(i)
    if len(ind)==1:
        return len(x)
    for i in ind:
        curr=abs(curr-i)
        re=max(re,curr)
    return re
nums=[9,1,4,7,3,-1,0,5,8,-1,6]
print(longestConsecutive(nums))