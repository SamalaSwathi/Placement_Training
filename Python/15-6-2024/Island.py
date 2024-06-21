"""
ip:  5
     0 1 0 0 1
     1 0 0 1 1 
     0 0 0 0 0 
     1 0 0 0 0 `           
     1 0 0 0 1

op:  5
"""


def fun(l,i,j,n): 
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return 
    l[i][j]=2
    fun(l,i-1,j,n)
    fun(l,i,j-1,n)
    fun(l,i+1,j,n)
    fun(l,i,j+1,n)
    return 

n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a) 
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
            fun(l,i,j,n)
print("Number of Islands:",count)