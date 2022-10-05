r =int(input("enter the row:"))
for i in range(1, r+1):
  for j in range(1, i+1):
    print("*", end = " ")
  print("\n")
x = r
for j in range(1, r):
  for i in range(1, x):
    print("*", end = " ")
  x = x - 1
  print("\n")
print("robert")
