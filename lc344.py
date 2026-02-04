def rev(list):
    left,right=0,len(list)-1
    while left<right:
        temp=list[left]
        list[left]=list[right]
        list[right]=temp
        left+=1
        right-=1
    return list
list=["h","e","l","l","0"] 
print(rev(list))   