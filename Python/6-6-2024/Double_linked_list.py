import math
class node:
    def __init__(self,x):
        self.next=None
        self.data=x
        self.prev=None

class  dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    
    def revdisplay(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="<-")
            t=t.prev
        print()

    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            #self.tail.next=node(x)
            #self.tail.next.prev=self.tail
            #self.tail=self.tail.next
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next

    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            #self.head.prev=node(x)
            #self.head.prev.next=self.head
            #self.head=self.head.prev
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            if(t.data==x or t1.data==x):
                print("Element found")
                break
            t=t.next
            t1=t1.prev
        else: 
            if(t.data==x):
                print("Element found")
            else:
                print("Element not found")
    
    def length(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            print("Odd length")
        else:
            print("Even length")

    def palindrome(self):
        t=self.head
        t1=self.tail
        c=0
        while(t!=t1 and t!=t1.next):
            if(t.data!=t1.data):
                print("Not palindrome") 
                break
            t=t.next
            t1=t1.prev
        else:
            print("Palindrome")

    def swaphalf(self):
        f=self.head
        s=self.head
        while(f!=None):
            f=f.next.next
            s=s.next
        f=self.head
        while(s!=None):
            s.data,f.data=f.data,s.data
            s=s.next
            f=f.next

    def pair(self):
        t=self.head 
        while(t!=None):
            t1=t.next
            if(t==self.head):
                t.next,t1.next=t1.next,t
                t.prev,t1.prev=t1,None 
                t.next.prev=t
                self.head=t1
            else:
                t.next,t1.next=t1.next,t
                t1.prev,t.prev=t.prev,t1
                if(t.next!=None):
                    t.next.prev=t
                t1.prev.next=t1    
            t=t.next
        
    def evenodd(self,t,e,o):
        if(t==None):
            return abs(e-o)  
        if(t.data%2==0):
            e=e+t.data
        else:
            o=o+t.data
        return self.evenodd(t.next,e,o) 
            
    def number(self,num,i):
        if(num==0 or num==1):
            return 0
        if(i>math.sqrt(num)): 
            return 1
        if(num%i==0): 
            return 0
        return self.number(num,i+1)
        
    def prime(self,t,c):
        if(t==None):
            return c
        if self.number(t.data,2):
            c=c+1  
        return self.prime(t.next,c)

                   
l1=dll()
l1.addback(11)
l1.addback(2)
l1.addfront(3)
l1.addback(13)
l1.addfront(8)
l1.addfront(27)
l1.display()
l1.revdisplay()
l1.search(90)
l1.length()
l1.palindrome()
l1.display()
l1.swaphalf()
l1.display()
l1.pair()
l1.display()
a=l1.evenodd(l1.head,0,0)
print(a)
b=l1.prime(l1.head,0)
print(b)