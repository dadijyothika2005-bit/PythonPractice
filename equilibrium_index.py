a=[2,4,6,3,2,1]
p=[0]
for x in a:
    p.append(p[-1]+x)
for i in range(len(a)):
    left=p[i]
    right=p[len(a)]-p[i+1]
    if(left==right):
        print(i," is equilibrium index.")


