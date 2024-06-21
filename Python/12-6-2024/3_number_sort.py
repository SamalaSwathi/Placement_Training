"""
Sorting the consecutive 3 numbers in the given list

ip: [4, 9, 8, 2, 14, 3, 5, 6]
op: [4, 2, 8, 3, 5, 6, 9, 14]
"""
l=list(map(int,input().split())) 
for i in range(len(l)-2):
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
    if l[i+1]>l[i+2]:
        l[i+1],l[i+2]=l[i+2],l[i+1]
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print(l)