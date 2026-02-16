def twoSum(nums, target):
      Sum_map={}
      diff=0
      for i,val in enumerate(nums):
         diff=target-val
         if diff in Sum_map:
            return [Sum_map[diff],i]
         Sum_map[val]=i   
      return Sum_map
nums=[2,3,5,6]
print(twoSum(nums,8))