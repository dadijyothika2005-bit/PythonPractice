import math
def add(x,y): return x+y
def sub(x,y): return x-y
def mul(x,y): return x*y
def div(x,y): return float(x/y)
def sqrt_(x): return math.sqrt(x)
def pow(x,y): return x**y
def log_(x):
    if x>0 : return math.log(x) 
    else: print("Enter positive number")
def tan_(x): return math.tan(math.radians(x))
def sin_(x): return math.sin(math.radians(x))
def cos_(x): return math.cos(math.radians(x))
while True:
    x=input("Enter number 1(+),2(-),3(*),4(/),5(sqrt),6(power),7(log),8(tan),9(cos),10(sin) and q(quit)\n")
    if x.lower()=="q":
       break
    if x in ('1','2','3','4','5','6','7','8','9','10'):
        if x=="1":
          a=int(input("enter number1:"))
          b=int(input("enter number2"))
          print(add(a,b))
        elif x=="2":
          a=int(input("enter number1:"))
          b=int(input("enter number2"))
          print(sub(a,b))
        elif x=="3":
          a=int(input("enter number1:"))
          b=int(input("enter number2"))
          print(mul(a,b))
        elif x=="4":
          a=int(input("enter number1:"))
          b=int(input("enter number2"))
          print(div(a,b))
        elif x=="5":
          a=int(input("enter number:"))
          print(sqrt_(a))
        elif x=="6":
          a=int(input("enter number1:"))
          b=int(input("enter number2"))
          print(pow(a,b))
        elif x=="7":
          a=int(input("enter number:"))
          print(log_(a))       
        elif x=="8":
          a=int(input("enter number:"))
          print(tan_(a))    
        elif x=="9":
          a=int(input("enter number:"))
          print(cos_(a)) 
        else:
          a=int(input("enter number:"))
          print(sin_(a)) 
    else:
       print("Invalid number! Try again.")