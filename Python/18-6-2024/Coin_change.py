"""
Minimum number of coins needed from the list to make the given amount
ip: [4, 3, 7]
    16
op: 4

ip: [1,3,4,5]
    17
op: 4

"""

l=list(map(int,input().split()))
n=int(input())
a=[0] 
for i in range(n):
    a.append(-1) 
for i in range(len(l)):
    for j in range(1,len(a)): 
        if l[i]<=j:
            m=j-l[i]
            if a[m]!=-1:   
                if a[j]!=-1:
                    a[j]=min(a[j],a[m]+1)
                else:
                    a[j]=a[m]+1 
print(a)
print(a[-1])