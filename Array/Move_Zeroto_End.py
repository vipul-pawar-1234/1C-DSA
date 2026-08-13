arr = [3,0,1,0,2,0]

new = []

for i in arr:
    if i!=0:
        new = new + [i]

for i in arr:
    if i == 0:
        new = new + [i]

print(new)