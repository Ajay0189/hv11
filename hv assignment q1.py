x=open("q1","a")
a=int(input("Enter First number:"))
b=int(input("Enter Second number:"))
c=int(input("Enter Third number:"))
d=int(input("Enter Fourth number:"))
e=int(input("Enter fifth number:"))
print("The Numbers are:",a,b,c,d,e)
print("The Numbers are:",a,b,c,d,e,file=x)
if (a<0) or (b<0) or (c<0) or (d<0) or (e<0):
    print("Enter positive numbers only")
    print("Enter positive numbers only",file=x)
else:
    result=a+b+c+d+e
    print("Sum of numbers is:",result)
    print("Sum of numbers is:",result,file=x)
    x.close()