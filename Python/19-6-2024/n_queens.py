def queen(r,co):
    if(r==n):
        return co
    if r!=u:
        for c in range(n):
            if(check(r,c)):
               m[r][c]=1
               co=co+1
               break
            m[r][c]=0 #when coming back in recursion
        return queen(r+1,co)
    else:
        queen(r+1,co)
def check(i,j):
    if(j==v):
        return 0
    r,c=i,j
    for i in range(r+1): #check for rows col is const
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
   
n=int(input())
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)

print(queen(0,0))
print(m)