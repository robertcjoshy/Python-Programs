l1=[]
l2=[]
import math
for i in range(1000,2000):
 if(i%2==0):
  l1.append(i)
print(l1)
for j in l1:
 y=int(math.sqrt(j))
 if(y*y==j):
  l2.append(j)
print(l2)
