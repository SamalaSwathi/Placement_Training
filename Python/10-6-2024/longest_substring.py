"""
length of longest substring without repeating charcters
ip: abfgresagtyuiofde
op: 12
"""

a=input() 
s=""                   
d={} 
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if a[i] not in s:
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=(d[a[i]])+1
print(m)






