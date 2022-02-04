t=int(input())
for i in range(t):
    a,b,c,p,q,r=map(int,input().split())
    minim=(a+b+c)-min(a,b,c)
    maxim=(p+q+r)-max(p,q,r)
    final=minim+maxim
    if final/2>maxim/2:
        print("YES")
    else:
        print("NO")