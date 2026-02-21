def replaceElements(arr):
       max_right=-1
       for i in range(len(arr)-1,-1,-1):
         val=arr[i]
         arr[i]=max_right
         if val>max_right:
            max_right=val
       return arr
arr=[2,4,5,1,3,2]      
print(replaceElements(arr))