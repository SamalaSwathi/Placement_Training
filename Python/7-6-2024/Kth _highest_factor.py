n=12
l=[]
k=4
max1=0
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)
v=l[-k:-k+1]
for i in v:
    print(i)