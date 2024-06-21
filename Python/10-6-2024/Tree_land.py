"""
ip: 6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0 
    0 0 0 1 1 1
    1 1 0 0 0 1 
    1 1 1 0 1 0 
    4 6

op: 8
"""

def fun(l,i,j,n): 
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return
    if l[i][j]==1:
        l[i][j]=2
    fun(l,i-1,j,n)
    fun(l,i,j-1,n)
    fun(l,i+1,j,n)
    fun(l,i,j+1,n)
    return 

n=int(input())
l=[]
co=0
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(int(input()))
    l.append(l1)
r=int(input())
c=int(input())  
fun(l,r-1,c-1,n) 
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            co=co+1
print(l)
print("Trees:",co)
