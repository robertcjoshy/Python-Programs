r = int(input("enter the row:"))
for i in range(1, r+1):
  for j in range(1, i+1):
    print(i*j, end = " ")
  print("\n")
