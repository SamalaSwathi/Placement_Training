#Checking whether a number can be divided into sum of 2 prime numbers

def isprime(x):
    if x==1:
        return 1
    if (x==2):
        return 1
    else:
        for i in range(2,(x//2)+1):
            if(x%i==0):
                return 0
        return 1

n=int(input())
for i in range(1,(n//2)+1):
    if(isprime(i) and isprime(n-i)):
        print("Yes")
        break
else:
    print("No")