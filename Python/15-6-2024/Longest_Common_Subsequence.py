"""
ip: abcd
    axbd
    
op: 3
"""
s=""
a=input()
b=input()
dp=[]
u=len(a)
v=len(b)
for i in range(len(a)+1):
    l=[0]*(len(b)+1)
    dp.append(l)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
while u>0 and v>0:
    if(a[u-1]==b[v-1]):
        s=s+a[u-1]
        u=u-1
        v=v-1
    else:
        if dp[u][v]==dp[u][v-1]: 
            v=v-1
        else:
            u=u-1
print(s[::-1])
print(dp[len(a)][len(b)])
print(dp)