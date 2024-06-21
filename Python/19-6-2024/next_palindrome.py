m=int(input())
n=m
z=""
z1=""
def palin(n):
    rev=0
    while n>0:
       r=n%10
       rev=rev*10+r
       n=n//10
    if rev==m:
        return 1
    else:
       return 0
if palin(n):
    print(m)
else:
    x=str(m)
    if len(x)%2==0:
        y=x[:len(x)//2]
        y=y+"".join(reversed(y))
        if int(y)>m:
            print(y)
        else:
            y=x[:len(x)//2]
            y=int(y)+1
            y=str(y)
            y=y+"".join(reversed(y))
            print(y)
    else:
        y=x[:len(x)//2]
        z=z+"".join(reversed(y))
        y=y+(x[(len(x)//2)])
        y=y+z
        if int(y)>m:
            print(y)
        else:
            y=x[:len(x)//2]
            z1=z1+"".join(reversed(y))
            y=y+str(int((x[(len(x)//2)]))+1)
            y=y+z1
            print(y)
