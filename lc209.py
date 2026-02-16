def minSubArrayLen( target, nums):
       minimum=float('inf')
       length=0
       curr_sum=0
       if(len(nums)<1):
        return 0
       left=0
       if(sum(nums)<target):
         return 0
       for right in range(len(nums)):
          curr_sum=curr_sum+nums[right]
          while(curr_sum>=target):
            length=right-left+1
            minimum=min(minimum,length)
            curr_sum=curr_sum-nums[left]
            left+=1
       return minimum   
nums=[2,3,1,2,4,3]
print(minSubArrayLen(7,nums))
