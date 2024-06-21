""" Palindrome using recursion"""


def palin(n,s):
    if(n==0):
        return s  
    s=(s*10)+(n%10)
    return palin(n//10,s)

n=int(input())
t=n
if(n==palin(n,0)):
    print("Yes")
else:
    print("No")