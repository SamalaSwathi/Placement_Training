'''  
from the given strings extract the  unique numbers and form the largest even number
ip:tu5g2k1h8
   g5g8gd6h3
op:865312

ip: tu5g9k1h7
    g5g1gd7h3 
op: -1
'''

a=input()
b=input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
    if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
print(d)
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(c)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
    else:
        print(-1)