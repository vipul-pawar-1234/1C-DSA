list = [3,2,6,4,8,5]
print("Before swipting",list)
size = len(list)


m = int(input("Enter swaping position times:"))

for c in range(m):
  x = list[0]
  for i in range (1,size):
    list[i-1] = list[i]
  list[size-1] = x
  
print("After sifhting 1 position",list)

