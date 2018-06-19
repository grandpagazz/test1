#coding=utf-8
#设计一个程序求出所有能够被7整除的3位整数
a=100
while a<1000:
    if a%7==0:
        print(a)
    a=a+1


#有一个10米深的井，井底有只青蛙，青蛙每天白天向上爬5米，但是晚上下滑3米
#设计一个程序计算青蛙需要几天能爬到井外
h=0
d=0
while h<10:
    h=h+5
    d=d+1
    if h>=10:
        print(d)
    else:
        h=h-3
        
#一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。
#设计一个程序计算它在第10次落地时，共经过多少米？第10次反弹多高？
h=100
s=100
times=0
while times<9:
    h=h/2
    s=s+h*2
    times=times+1
print(h/2)
print(s)


#猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个。
#第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。
#设计一个程序计算第一天共摘了多少个
num=1
times=0
while times<9:
    num=num+1
    num=num*2
    times=times+1
print(num)



#猜数字：设计一个程序，程序内部设置一个数值，让用户猜这个值是多少（可以提示用户猜的值与预设的值大小关系）
num=60
user=0
times=0
while user!=num and times<5:
    print("请输入一个数字：")
    user=int(input())
    if user==num:
        print("相等")
    elif user>num:
        print("大")
    else:
        print("小")
    times=times+1


#判断是否构成三角形，如果能构成，判断构成什么类型三角形，如果不能构成，则继续输入
a=1
b=2
c=3
result=a+b>c and a+c>b and b+c>a
while result==False:
    print("请输入第一个数据：")
    a=input()
    a=int(a)
    print("请输入第二个数据：")
    b=int(input())
    print("请输入第二个数据：")
    c=int(input())
    result=a+b>c and a+c>b and b+c>a
    if result==True:
        if a==b and b==c and a==c:
            print("等边三角形")
        elif a==b or b==c or a==c:
            print("等腰三角形")
        else:
            print("普通三角形")
    else:
        print("不能构成三角形")



        
