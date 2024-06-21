"""
ip: school
    3
    L 2
    R 3
    L 1
    
op: yes
"""

s=input()
n=int(input())
p=[]
a=[]
for i in range(n):
    b=input() 
    if(b[0]=='L'):
        a.append(s[int(b[2])])
    else:
        a.append(s[-int(b[2])])
a=list(a)
a.sort()
for i in range(len(s)-n+1): 
    t=list(s[i:n+i])
    t.sort()
    p.append(t) 
for i in p:
    if i==a:
        print("Yes")
        break
else:
    print("No")
    