
def prime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

def fun(i,j):  
    for k in range(j-1,i,-1):
        if prime(k):
            return k
    return 0
l=list(map(int,input().split()))
s=0
for i in range(len(l)-1): 
    s=s+fun(l[i],l[i+1])
print(s)