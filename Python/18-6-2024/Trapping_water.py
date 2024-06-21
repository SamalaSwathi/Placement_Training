"""
ip: 2 5 2 3 6 7 1 0 5 7
op: 20

ip: 4 3 4 5 6 1 0 6 7
op: 12
"""

l=list(map(int,input().split()))
a=[0]*len(l)
d=[0]*len(l)
m=0
s=0
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
    a[i]=m
m1=0 
for i in range(len(l)-1,-1,-1):
    if l[i]>m1:
        m1=l[i]
    d[i]=m1
for i in range(len(l)):
    s=s+((min(a[i],d[i]))-l[i])
print(a)
print(d)
print(s)