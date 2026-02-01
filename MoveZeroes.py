
def moveZeroes( nums):
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0
        print(nums)
nums=[1,0,2,2,1,1,0] 
moveZeroes(nums) 
      