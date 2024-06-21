class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def inorder(self,root): 
        if(root):
            self.inorder(root.left) 
            print(root.data,end=" ")
            self.inorder(root.right) 

    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

    def preorder(self,root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def create(self,root,x): 
        if(root is None):
            return node(x)
        elif(x < root.data):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x) 
        return root
    
    def sum(self,root):
        if(root): 
            return self.sum(root.left) + self.sum(root.right) + root.data
        else:
            return 0
        
    def even(self,root):
        if(root==None):
            return 0
        if(root.data %2==0):
            return root.data + self.even(root.left) + self.even(root.right)
        else:
            return self.even(root.left) + self.even(root.right)
        
    def odd(self,root):
        if(root==None):
            return 0
        if(root.data %2!=0):
            return root.data + self.odd(root.left) + self.odd(root.right)
        else:
            return self.odd(root.left) + self.odd(root.right)
    
    def evenodd(self,root):
        if(root==None):
            return 0
        if(root.data %2==0):
            return self.evenodd(root.left) + self.evenodd(root.right) + root.data
        return self.evenodd(root.left) + self.evenodd(root.right) - root.data
    
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    
    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
        
    def leaf(self,root):
        if root==None: 
            return 0 
        if root.left==None and root.right==None: 
            return 1
        return self.leaf(root.left)+self.leaf(root.right)
    
    def leafsum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None: 
            return root.data
        return self.leafsum(root.left)+self.leafsum(root.right)
    
    def search(self,root,x):
        if root==None:
            return False
        if root.data==x:
            return True
        elif x>root.data:
            return self.search(root.right,x)
        elif x<root.data:
            return self.search(root.left,x)
        
    def depth(self,root,x,c):
        if root==None:
            return -1
        if(self.search(root,x)):
            if root.data==x:
                return c
            elif x>root.data:
                c=c+1
                return self.depth(root.right,x,c)
            elif x<root.data:
                c=c+1
                return self.depth(root.left,x,c)
    
    def top(self,root):
        if root==None:
            return
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if root.left!=None: 
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            if q[0][1] not in d:
                d[q[0][1]]=root.data
            q.pop(0)    
        for i in sorted(d):
            print(d[i],end=" ")
    
    def bottom(self,root):
        if root==None:
            return
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if root.left!=None: 
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)          
        for i in sorted(d):
            print(d[i],end=" ")

    def right(self,root,c,l):
        if root==None:
            return 
        if c not in l:
            print(root.data,c)
            l.append(c)
        self.right(root.right,c+1,l)
        self.right(root.left,c+1,l) 
        
    def left(self,root,c,l):
        if root==None:
            return
        if c not in l:
            print(root.data,c)
            l.append(c)
        self.left(root.left,c+1,l)
        self.left(root.right,c+1,l)
         
t1=tree()
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,11)
t1.create(t1.root,20)
t1.create(t1.root,4)
t1.create(t1.root,3)
t1.create(t1.root,12)
t1.create(t1.root,13)
t1.create(t1.root,14)
t1.inorder(t1.root)
print()
t1.postorder(t1.root)
print()
t1.preorder(t1.root)
print()
print("Total sum:",t1.sum(t1.root))
print("Leftsubtree-Rightsubtree:",t1.sum(t1.root.left)-t1.sum(t1.root.right))
print("Evensum:",t1.even(t1.root))
print("Oddsum:",t1.odd(t1.root))
print("Evensum-Oddsum:",abs(t1.evenodd(t1.root)))
print("Height:",t1.height(t1.root))
if(t1.balance(t1.root)):
    print("Balanced")
else:
    print("Not balanced")
print("Number of leaf nodes:",t1.leaf(t1.root))
print("Sum of leafnodes:",t1.leafsum(t1.root))
print(t1.search(t1.root,11))
print(t1.depth(t1.root,4,0))
print("Top View:")
t1.top(t1.root)
print()
print("Bottom View:")
t1.bottom(t1.root)
print()
print("Right View:")
t1.right(t1.root,0,[])
print("Left View:",)
t1.left(t1.root,0,[])
print() 