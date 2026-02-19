def duplicate(nums,k):
    prev_ind=0
    seen={}
    for i in range(len(nums)):
       curr_num=nums[i]
       if curr_num in seen:
            prev_ind=seen[curr_num]
            if abs(i-prev_ind)<=k :
                return True
       seen[curr_num]=i
    return False
nums=[1,1,2,3]
print(duplicate(nums,2))        
    