"""
printing a list that contains set of lists with distinct numbers from the main list

ip: [1,2,3,4,1,2,3,1,2]
op: [[1,2,3,4],[1,2,3],[1,2]]

ip: [4,5,2,1]
op: [[4,5,2,1]]

ip: [2,3,1,3,4,3,2]
op: [[2,3,1,4],[3,2],[3]]
"""

"""
l=list(map(int,input().split()))
s=[]
c=0
while(c!=(len(l))):
    a=[]
    for i in range(len(l)): 
        if (not str(l[i]).isalpha()):
            if l[i] not in a:
                c=c+1
                a.append(l[i])
                l[i]='a'
    s.append(a)  
print(s)

"""


l=list(map(int,input().split()))
s=[]
d={}
c=0
for i in l:
    if(i not in d):
       d[i]=1
    else:
        d[i]=d[i]+1
while(c!=(len(l))):
    a=[]
    for i in d: 
        if d[i]!=0:
            d[i]=d[i]-1
            a.append(i)
            c+=1
    s.append(a)
print(s)