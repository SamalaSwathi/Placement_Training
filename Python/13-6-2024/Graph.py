def dfs(j,l):
    l.append(j)
    for i in d[j]:
        if i not in l:
            dfs(i,l)
    return l
    
def path(s,e,l,c):
    l.append(s)
    if s==e:
        print(l) 
        c=c+1
        l.pop()
        return c
    for i in d[s]:
        if i not in l:
            c=path(i,e,l,c)
    l.pop()
    return c
    
def path_cost(s,e,l,co):
    l.append(s)
    if s==e:
        print(l,co)
        l.pop() 
        return
    for i in d1[s]:
        if i[0] not in l:  
            path_cost(i[0],e,l,co+i[1])
    l.pop()
    
def mincost(s,e,l,co,m,l1):
    l.append(s)
    if s==e: 
        if co<m:
            m=co
            l1=l.copy()
        l.pop() 
        return m,l1
    for i in d1[s]:
        if i[0] not in l:  
            m,l1=mincost(i[0],e,l,co+i[1],m,l1)
    l.pop()
    return m,l1

def allpaths(s,e,l):
    l.append(s)
    if s==e:
        print(l) 
        l.pop() 
        return
    for i in d[s]:
        if i not in l:
            allpaths(i,e,l)
    l.pop()

def allpathsmincost(s,e,l,co,m,l1):
    l.append(s)
    if s==e: 
        if co<m:
            m=co
            l1=l.copy()
        l.pop() 
        return m,l1
    for i in d1[s]:
        if i[0] not in l:  
            m,l1=allpathsmincost(i[0],e,l,co+i[1],m,l1)
    l.pop()
    return m,l1

def bfs(j):
    q=[j]
    v=[] 
    while(q):
        for i in d[q[0]]:
            if (i not in q) and (i not in v):
                q.append(i)
        v.append(q[0])
        q.pop(0) 
    return v

d1={5:[(7,11),(3,10)],7:[(5,11),(4,12),(3,14)],4:[(7,12),(8,10),(2,13)],8:[(3,15),(4,10),(2,16)],3:[(5,10),(7,14),(8,15)],2:[(4,13),(8,16)]}
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
d2={1:[2,3,4],2:[1,4,6],3:[1,4],4:[1,2,3,5,6],5:[4],6:[2,4,7],7:[6]}
print("Dfs:", dfs(5,[]))
print("Paths:")
print("Total paths:",path(5,2,[],0))
path_cost(5,2,[],0)
print("Min. cost path:",mincost(5,2,[],0,999999,[]))
print("All possible paths:")
for i in d: 
    allpaths(5,i,[])
print("Minimum cost of all paths:")
for i in d.keys():
    print(allpathsmincost(5,i,[],0,999999,[]))
print("Bfs:",bfs(5))