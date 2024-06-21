"""
ip: MMMFMFMFMFFMFMMFMF
op: M
"""
a=input()
count,count1=0,0
for i in a:
    if i=='M':
        count=count+1
    elif i=='F':
        count1=count1+1
if count==count1:
    print("0")
elif count>count1:
    print("M")
else:
    print("F")