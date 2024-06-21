"""   
   ip:   
         xyzabcdefklmnopqefgh               print the length of longest substring
   op:
         7 
"""

s="abcdeklmnop"
s=list(s)
m=0
c=1
for i in range(len(s)-1):
    if((ord(s[i+1])-ord(s[i]))==1):
        c=c+1
    else:
        c=1
if(c>m):
    m=c
print(m)
