#Adding even numbers from first numbers and odd numbers from second list and appending their sum into a list

def fun(i):
    if i==len(l):
        return 
    if l[i]%2==0:
        def fun2(a,r,j,s,b):
            if j==len(a):
                r.append(s)
                return 
            if a[j]%2!=0:
                b.append(l[i]+a[j])
                s=s+l[i]+a[j] 
            fun2(a,r,j+1,s,b) 
        fun2(a,r,0,s,b) 
        fun(i+1)
    else: 
        fun(i+1)

l=[6,3,2,9,4,7]
a=[8,7,5,3,6,9]
r=[]
b=[]
s=0
fun(0) 
print(b)
print(r)
