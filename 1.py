#���һ��������������ܹ���7������3λ����
a=100
while a<1000:
    if a%7==0:
        print(a)
    a=a+1


#��һ��10����ľ���������ֻ���ܣ�����ÿ�����������5�ף����������»�3��
#���һ���������������Ҫ��������������
h=0
d=0
while h<10:
    h=h+5
    d=d+1
    if h>=10:
        print(d)
    else:
        h=h-3
        
#һ���100�׸߶��������£�ÿ����غ�����ԭ�߶ȵ�һ�룬�����¡�
#���һ������������ڵ�10�����ʱ�������������ף���10�η�����ߣ�
h=100
s=100
times=0
while times<9:
    h=h/2
    s=s+h*2
    times=times+1
print(h/2)
print(s)


#���ӵ�һ��ժ�����ɸ����ӣ���������һ�룬����񫣬�ֶ����һ����
#�ڶ��������ֽ�ʣ�µ����ӳԵ�һ�룬�ֶ����һ����
#�Ժ�ÿ�����϶�����ǰһ��ʣ�µ�һ����һ��������10���������ٳ�ʱ����ֻʣ��һ�������ˡ�
#���һ����������һ�칲ժ�˶��ٸ�
num=1
times=0
while times<9:
    num=num+1
    num=num*2
    times=times+1
print(num)



#�����֣����һ�����򣬳����ڲ�����һ����ֵ�����û������ֵ�Ƕ��٣�������ʾ�û��µ�ֵ��Ԥ���ֵ��С��ϵ��
num=60
user=0
times=0
while user!=num and times<5:
    print("������һ�����֣�")
    user=int(input())
    if user==num:
        print("���")
    elif user>num:
        print("��")
    else:
        print("С")
    times=times+1


#�ж��Ƿ񹹳������Σ�����ܹ��ɣ��жϹ���ʲô���������Σ�������ܹ��ɣ����������
a=1
b=2
c=3
result=a+b>c and a+c>b and b+c>a
while result==False:
    print("�������һ�����ݣ�")
    a=input()
    a=int(a)
    print("������ڶ������ݣ�")
    b=int(input())
    print("������ڶ������ݣ�")
    c=int(input())
    result=a+b>c and a+c>b and b+c>a
    if result==True:
        if a==b and b==c and a==c:
            print("�ȱ�������")
        elif a==b or b==c or a==c:
            print("����������")
        else:
            print("��ͨ������")
    else:
        print("���ܹ���������")



        
