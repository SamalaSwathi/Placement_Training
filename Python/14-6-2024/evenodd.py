#Adding even numbers from first numbers and odd numbers from second list and appending them into a list

def fun(i):
    if i==len(l):
        return 
    if l[i]%2==0:
        def fun2(a,r,j):
            if j==len(a):
                return 
            if a[j]%2!=0:
                r.append(l[i]+a[j]) 
            fun2(a,r,j+1) 
        fun2(a,r,0)
        fun(i+1)
    else: 
        fun(i+1)

l=[6,3,2,9,4,7]
a=[8,7,5,3,6,9]
r=[]
fun(0) 
print(r)