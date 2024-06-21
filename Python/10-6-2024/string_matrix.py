"""
check whether the given string present in the string matrix or not

ip: 4
    t u e d
    f w o w
    r o o r
    d r k i
    word
op: Yes

"""


def fun(i,j,k,t):
    if(k==len(s)):
        return 1
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=s[k]):
        return 
    if(l[i][j]==s[k]):
        l[i][j]=0
    if t!=1:
        t=fun(i+1,j,k+1,t)
        t=fun(i-1,j,k+1,t)
        t=fun(i,j-1,k+1,t)
        t=fun(i,j+1,k+1,t)
    return t
n=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(input())
    l.append(l1)
s=input()
for i in range(n):
    for j in range(n):
        if l[i][j]==s[0]:
           c=fun(i,j,1,0)
           if(c==1):
               print("Yes")
               break
if c==0:
    print("No")