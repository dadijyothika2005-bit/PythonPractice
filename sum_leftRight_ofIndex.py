a=[4,1,2,3]
p=[0]
for x in a:
    p.append(p[-1]+x)
print(p)
for i in range(len(a)):
    print("Sum of elements to the left of ",i," is ",p[i])
    print("Sum of elements to the right of ",i," is ",p[len(a)]-p[i+1])