l=[10,20,30,40,50]
print(l[0])
print(l[-1])
print(l)
l.append(60)
l.append(70)
print(l)
print(l.pop())
for i in l:
    print(i)
n=list(map(int,input().split()))

print("Even numbers: ")
for i in n:
    if i%2==0 :
       print(int(i))
n1=[]
for i in n:
     x=i*i
     n1.append(x)

print(n1) 
n2=[] 
for i in n1:
    if i>10:
        n2.append(i)
print(n2)