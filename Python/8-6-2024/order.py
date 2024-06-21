"""
Printing numbers according to the alphabetical order given

ip:
   2
   polikujmnhytgbvfredcxswqaz
   abcd
   qwryupcsfoghjkldezxvbintma
   ativedoc

op:  
   bdca
   codevita
"""

n=int(input())
while(n):
    a=input()
    c=input()
    s=""
    for i in a:
        if i in c:
            s=s+(i*c.count(i))
    print(s)
    n=n-1
