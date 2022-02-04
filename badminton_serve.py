t=int(input())
for i in range(t):
    cnt=0
    p=int(input())
    for j in range(p+1):
        if j%2==0:
            cnt+=1
    print(cnt)


