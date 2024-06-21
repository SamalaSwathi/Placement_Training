
"""  
check whether every alphabet in the given string is taken from the string matrix in order or not

  ip:                            ip:
        3                             4
        xyz                           abcd
        pqr                           xyze
        abc                           pqrw
        "yraxpazr"                    stuv
  op:                                 "cyptdzsayq"
        yes                      op:
                                       no
"""

n=int(input())
m=[]
f=0
for i in range(n):
    m.append(list(input()))
s=input()
for i in range(len(s)):
    if s[i]  not in m[i%n]:
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
        
if(f==1):
    print("no")
else:
    print("yes")
