def dijkstra(s):
    d1={1:999,2:999,3:999,4:999,5:999}
    d1[s]=0
    v=[]
    q=[s]
    while(q):
        m=9999
        for i in q:
            if d1[i]<m:
                m=d1[i]
                s=i
        for i in d[s]:
            if i[0] not in v:
                if d1[i[0]]>(d1[s]+i[1]):
                    d1[i[0]]=d1[s]+i[1]
                if i[0] not in q:
                    q.append(i[0]) 
        v.append(s)  
        q.remove(s)
    return (d1)

d={1:[(2,2),(3,2),(4,1)],2:[(1,2),(4,2),(5,3)],3:[(1,2),(4,3)],4:[(1,1),(2,2),(3,3),(5,2)],5:[(2,3),(4,2)]}
print("Dijkstra:",dijkstra(1))