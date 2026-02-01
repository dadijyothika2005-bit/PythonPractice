
def removeElement( nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        print(k)
        print(nums[0:k])
nums=[3,2,5,3,1]
removeElement(nums,3)