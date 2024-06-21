#add the numbers in the given number until the sum is <=9 and check whether the sum is prime or not
#if it is not a prime number print the next number to the input

def add(n):
    s=0
    while(n):
        s=s+(n%10)
        n=n//10
    return s

def pnp(n):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1


n=int(input())
m=n
if (n<10):
    print(pnp(n))
else:
    while(1):
        n=add(n)
        if(n<10):
            break
    print(pnp(n))