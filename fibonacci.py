
a=0 #variable declearation
b=1
num=int(input("enter the number for fibonacci series :"))
if num==1:
    print(a)
else:
    print(a)
    print(b)
for i in range(1,num+1):
    c=a+b # a+b is assigned in c variable.
    a=b # a is replaced on the place of b.
    b=c # b is replaced on the place of c.
    print(c)