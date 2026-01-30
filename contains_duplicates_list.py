l=list(map(int,input().split()))
a=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            a=1
            break   
    if a:
       break    
if a:        
 print("True")
else:
   print("False")                 