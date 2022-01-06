'''
You're given an integer N. Write a program to calculate the sum of all the digits of N.
'''
t=int(input())
for i in range(t):
    n=int(input())
    total=0
    while(n!=0):
        temp=int(n%10)
        total+= temp
        n=int(n/10)
    print(total)