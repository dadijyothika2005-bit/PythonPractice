a=[1,2,3,4,5]
p=[0]
for x in a:
    p.append(p[-1]+x)
for i in range(len(a)):
    for j in range(i,len(a)):
        print("Subarray: ",a[i:j+1]," sum is ",p[j+1]-p[i])    
        