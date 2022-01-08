'''
Kepler’s Law states that the planets move around the sun in elliptical orbits with the sun at one focus. Kepler's 3rd law is The Law of Periods, according to which:

The square of the time period of the planet is directly proportional to the cube of the semimajor axis of its orbit.
You are given the Time periods (T1,T2) and Semimajor Axes (R1,R2) of two planets orbiting the same star.

Please determine if the Law of Periods is satisfied or not, i.e, if the constant of proportionality of both planets is the same.

Print "Yes" (without quotes) if the law is satisfied, else print "No".
'''

t=int(input())
for i in range(t):
    t1,t2,r1,r2=map(int,input().split())
    if ((t1**2/r1**3)==(t2**2/r2**3)):
        print("Yes")
    else:
        print("No")