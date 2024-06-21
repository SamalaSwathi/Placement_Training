"""
Buying a pen and selling the pen for more profit

ip:  15 3 2 7 8 4                    ip:  5 4 2 9 7 1
     m  t w t f s  
op:  6                               op: 7


ip:   5 3 2 7 8 4                    ip:  9 8 7 6 5 4

op:   6                              op:  0

"""

l=[]
m1=0
for i in range(6):
    l.append(int(input()))
for i in range(len(l)-1):
    for j in range((i+1),len(l)):
        if(l[j]>l[i] and l[j]-l[i]>m1):
            m1=l[j]-l[i]
print("Profit: ",m1)

