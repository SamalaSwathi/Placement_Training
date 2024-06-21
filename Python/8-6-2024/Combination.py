#Print Three combination numbers

def three(l,k): 
    def fun(curr,start):
        if(len(curr)==k):
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
l=[3,2,5,4,1,6,8]
n=3
three(l,n)
