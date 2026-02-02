class NumArray(object):

    def __init__(self, nums):
        self.nums=nums
        self.p=[0]
        for x in self.nums:
         self.p.append(self.p[-1]+x)

    def sumRange(self, left, right):
     sum=self.p[right+1]-self.p[left]  
     return sum
nums=[-2,0,3,-5,2,-1]    
obj=NumArray(nums)
s1=obj.sumRange(0,2)   
s2=obj.sumRange(2,5)  
s3=obj.sumRange(0,5)  
print("[null,",s1,",",s2,",",s3,"]")