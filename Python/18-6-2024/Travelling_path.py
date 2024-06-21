"""
ip: 4*3 

    _ _ _ _
    _ _ _ _
    _ _ _ _
"""

def fun(i,j,co):
    if(i<0 or i>=a or j>=b or j<0):
        return co
    if i==a-1 and j==b-1:
        co+=1 
        return co
    vi.append((i,j))
    if((i-1,j) not in vi):
        co=fun(i-1,j,co)
    if((i,j-1) not in vi):
        co=fun(i,j-1,co)
    if((i+1,j) not in vi):
        co=fun(i+1,j,co)
    if((i,j+1) not in vi):
        co=fun(i,j+1,co) 
    vi.pop()
    return co

a=int(input())
b=int(input())
vi=[]
print(fun(0,0,0))