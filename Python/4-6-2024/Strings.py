"""
move every alphabet in the string backwards by the given number of steps

ip:                            ip:                          ip:
        khoor                           bvec                          bcdmnwc
        3                               4                             9
op:                            op:                          op:
        hello                           xray                          student
"""

str=input()
key=int(input())
s1=""
c=key%26
for i in str:
    if((ord(i)-c)>=97):
        s1=s1+chr(ord(i)-c)
    else:
        s1=s1+chr(ord(i)-c+26)
print(s1)
