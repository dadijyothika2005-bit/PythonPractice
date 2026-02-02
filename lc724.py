def pivotIndex( nums):
        t=sum(nums)
        left=0
        for i in range(len(nums)):
            if(left==t-left-nums[i]):
                return i
            left+=nums[i]
        return -1
nums=[1,7,3,6,5,6]
print(pivotIndex(nums))        