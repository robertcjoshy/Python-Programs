str = input("enter the string:")
count = dict()
for i in str:
  if i in count:
    count[i] = count[i] + 1
  else:
    count[i] = 1
print(count)
