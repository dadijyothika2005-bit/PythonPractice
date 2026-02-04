
def subarraySum( nums, k):
        counts={0:1}
        count=0
        sum=0
        for i in range(len(nums)):
               sum+=nums[i]   
               if sum-k in counts:
                       count+=counts[sum-k]
               counts[sum]=counts.get(sum,0)+1       
        return count            
nums=[1,2,3]   
k=3
print(subarraySum(nums,k))     