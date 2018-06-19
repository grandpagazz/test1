#coding=utf-8
a=100
while a<1000:
    if a%7==0:
        print(a)
    a=a+1

h=0
d=0
while h<10:
    h=h+5
    d=d+1
    if h>=10:
        print(d)
    else:
        h=h-3
        
h=100
s=100
times=0
while times<9:
    h=h/2
    s=s+h*2
    times=times+1
print(h/2)
print(s)


num=1
times=0
while times<9:
    num=num+1
    num=num*2
    times=times+1
print(num)


num=60
user=0
times=0
while user!=num and times<5:
    print("please insert a number：")
    user=int(input())
    if user==num:
        print("equal")
    elif user>num:
        print("big")
    else:
        print("small")
    times=times+1


a=1
b=2
c=3
result=a+b>c and a+c>b and b+c>a
while result==False:
    print("please insert 1st number：")
    a=input()
    a=int(a)
    print("please insert 2nd number：")
    b=int(input())
    print("please insert 3rd number：")
    c=int(input())
    result=a+b>c and a+c>b and b+c>a
    if result==True:
        if a==b and b==c and a==c:
            print("Equilateral triangle")
        elif a==b or b==c or a==c:
            print("isosceles triangle")
        else:
            print("Common triangle")
    else:
        print("Can't make up a triangle")



        
