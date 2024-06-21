class node:
    def __init__(self, u):
        self.data=u
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()

    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)

    def addfront(self,x):
        new=node(x)
        new.next=self.head
        self.head=new

    def evensum(self):
        t=self.head
        s1=0
        while(t!=None):
            if(t.data%2==0):
                s1=s1+t.data
            t=t.next
        print("Sum of even numbers:",s1)

    def search(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                print("Element Found")
                break
            t=t.next
        else:
            print("Element Not Found")

    def middle(self):
        s=self.head
        f=self.head
        while(f!=None and f.next!=None):
            s=s.next
            f=f.next.next
        print(s.data)
    
    def length(self):
        f=self.head
        while(f!=None and f.next!=None): 
            f=f.next.next
        if(f==None):
            print("Length is Even")
        else:
            print("Length is Odd")

    def substring(self):
        t=self.head
        c=1
        m=0
        while(t.next!=None):
            if(t.next.data-t.data)==1:
                c=c+1
                if(c>m):
                    m=c
            else:
                c=1
            t=t.next
        print(m)
    
    def pairs(self):
        t=self.head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next

    def bubble(self):
        t=self.head
        c=0
        p=None
        while(t.next!=None):
            f=0
            t1=self.head
            while(t1.next!=p):
                if(t1.data>t1.next.data):
                    f=1
                    t1.data,t1.next.data=t1.next.data,t1.data
                t1=t1.next
                c=c+1
            if(f==0):
                break
            p=t1
            t=t.next
        print("Iterations:", c)   

    def reverse(self):
        a=self.head


l1=sll()
l1.head=node(2)
l1.addback(4)
l1.addback(7)
l1.addback(6)
l1.addback(9)
l1.addfront(8)
l1.addback(13)
l1.addback(11)
l1.addback(12)
l1.display()
l1.evensum()
l1.search(100)
l1.middle()
l1.length()
l1.substring()
l1.pairs()
l1.bubble()
l1.display()
print()

l2=sll()
l2.head=node(10)
l2.addback(20)
l2.addback(345)
l2.addback(34)
l2.addfront(275)
l2.display()
l2.evensum()
l2.middle()
l2.length()
l2.bubble()
l2.display()