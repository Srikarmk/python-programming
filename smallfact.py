'''
Write a program to find the factorial value of any number entered by the user.
'''
import math 
t=int(input())
for i in range(t):
    n=int(input())
    fact=math.factorial(n)
    print(fact)