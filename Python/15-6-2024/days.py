"""
Convert days into years, months and weeks

ip: 
     65476
"""
#year=360
#months=30
#weeks=6
n=65
y=n//360
k=n%360
m=k//30
k1=k%30
d=k1%6
print(y,":years",m,":months",d,":days")