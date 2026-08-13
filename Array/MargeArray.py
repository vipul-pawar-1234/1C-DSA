l = int(input("Enter length of both arrays:"))
arr1 = []
arr2 = []
print("Enter 1st element number:")
for i in range(l):
    r = int(input())
    arr1 = arr1 + [r]

print("Enter 2nd element number:")
for i in range(l):
    r = int(input())
    arr2 = arr2 + [r]


print(arr1+arr2)