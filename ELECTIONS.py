'''
There are 101 citizens in Chefland. It is election time in Chefland and 3 parties, A,B, and C are contesting the elections. Party A receives XA votes, party B receives XB votes, and party C receives XC votes.

The constitution of Chefland requires a particular party to receive a clear majority to form the government. A party is said to have a clear majority if it receives strictly greater than 50 votes.

If any party has a clear majority, print the winning party (A, B or C). Otherwise, print NOTA.
'''
t=int(input())
for i in range(t):
    xa,xb,xc=map(int,input().split())
    if xa >50:
        print("A")
    elif xb>50:
        print("B")
    elif xc>50:
        print("C")
    else:
        print("NOTA")
        