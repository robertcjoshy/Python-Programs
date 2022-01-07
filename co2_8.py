l=["python", "java", "Cprogram"]
max=len(l[0])
temp=l[0]
for i in l:
 if(len(i)>max):
  max=len(i)
  temp=i
print("the longest word is:",temp)
print("length=", max)
