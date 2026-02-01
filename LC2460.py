
def applyOperations(nums):
        k=0
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]*=2
                nums[i+1]=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0       
        return nums   
nums=[1,0,2,2,1,1,0]
print(applyOperations(nums))
