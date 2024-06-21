

class node:
    def __init__(self):
        self.d={}
        self.flag=0

class tries:
    def __init__(self):
        self.root=node()

    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1 

    def search(self,str):
        t=self.root
        for i in str:
            if i in t.d:
                t=t.d[i]
            else: 
                return False
        if t.flag==1:
            return True
 
    def prefix(self,str):
        t=self.root
        for i in str:
            if i in t.d:
                t=t.d[i]
            else: 
                return False
        return True
    
    def all_prefix(self,str):
        def fun(t,s):
            if t.flag==1:
                print(s) 
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root 
        s=""
        for i in str:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return 
        fun(t,s)
    

t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if a=='1':
        t1.insert(s)
    elif a=='2':
        print(t1.search(s))
    elif a=='3':
        print(t1.prefix(s))
    elif a=='4':
        t1.all_prefix(s)             