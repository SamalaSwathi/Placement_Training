#Arrange words in a sentence according to the numbers
s="is2 sentence4 This1 a3"
s=s.split()
b=[0]*len(s)
for i in s:
    b[int(i[-1])-1]=i[:-1]
print(' '.join(b))