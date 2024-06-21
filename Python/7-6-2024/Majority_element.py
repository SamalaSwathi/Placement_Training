l=[1,5,3,3,3,3,6,3,7] 
c=1
w=l[0] 
for i in range(1,len(l)):
    if l[i]==w:
        c=c+1 
    else:
        c=c-1
        if c==0:
            c=1
            w=l[i]
print(w)















