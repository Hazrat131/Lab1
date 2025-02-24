import math
x=0.5
e=0.001
S=0
i=2
k=1
a=math.sin(x)
while abs(a) >= e:
    S=S+a
    k=k*(-1)
    a=(math.sin(x**i))/(i*(i+1))*k
    i=i+1
print(S)
    
    
