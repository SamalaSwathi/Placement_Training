"""
ip:  [(){}]
op:   -1

ip:  [{}(){[]}]
op:   -1

ip:  [({}]]
op:   5


"""

s=input()
l=[] 
f=0
c=0
for i in s: 
    if(i in '{[('):
        l.append(i)
    elif(not l):
        if((i==']' and l[-1]=='[') or (i=='}' and l[-1]=='{') or (i==')' and l[-1]=='(')):
            l.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
    c=c+1
if(f==0):
    print("-1")