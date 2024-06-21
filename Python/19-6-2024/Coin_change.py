'''
ip:   l=[2,3,5,6]
      11
op:   yes
'''
l=list(map(int,input().split()))
t=int(input())
m=[]
for i in range(len(l)+1):
    m.append([0]*(t+1))
for i in range(1,len(l)+1):
    for j in range(t+1):
        if j==0:
            m[i][j]=1
        elif l[i-1]>j:
            m[i][j]=m[i-1][j]
        else:
            if m[i-1][j]==0:
                x=j-l[i-1]
                m[i][j]=m[i-1][x]
            else:
                m[i][j]=m[i-1][j]

if m[len(l)][t]==1:
    print("yes")
else:
    print("no")