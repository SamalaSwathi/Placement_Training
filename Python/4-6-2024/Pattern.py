"""
ip: 5
op:  
     * * * * *
     * 1 2 3 *
     * 4 5 6 *
     * 7 8 9 *
     * * * * *
"""


n=int(input())
c=1
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==(n-1)):
            print("*",end=" ")
        elif(j!=(n-1)):
            print(c,end=" ")
            c=c+1
    print()



