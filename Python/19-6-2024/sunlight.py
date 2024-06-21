'''
on how many buildings will the sunlight falls in the evening and morning
ip:3 5 9 6 8 10

op:5
'''
arr=list(map(int,input().split()))

l=[0]*len(arr)
r=[0]*len(arr)
m=0
m1=0
for i in range(len(arr)):
    if(arr[i]>m):
        m=arr[i]
    l[i]=m
    
for i in range(len(arr)-1,-1,-1):
    if(arr[i]>m1):
        m1=arr[i]
    r[i]=m1
s=0
print(l)
print(r)
l1=set(l)
l2=set(r)
print(l1)
print(l2)
print(len(l1)+len(l2))
