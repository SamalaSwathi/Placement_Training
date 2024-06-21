"""
remove stars from the word
"""
a="leet**cod*e"
b=[]
for i in a:
    if(i!='*'):
        b.append(i)
    else:
        b.pop()
print(b)
print(''.join(b))    