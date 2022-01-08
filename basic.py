t=int(input())
for i in range(t):
    a,b,p,q=map(int,input().split())
    sum1=a+b
    sum2=p+q
    if(sum1==sum2):
        print("0")
    else:
        if(sum1%2==0 and sum2%2==0):
            print("2")
        elif(sum1%2!=0 and sum2%2!=0):
            print("2")
        elif(sum1%2!=0 and sum2%2==0):
            print("1")
        elif(sum1%2==0 and sum2%2!=0):
            print("1")
