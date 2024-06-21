
#Use recursion to print even numbers from 1 to n
def add(n):
    if(n==0):
        return 0
    return n+add(n-2)

n=13
if(n%2==0):
    print(add(n))
else:
    print(add(n-1))