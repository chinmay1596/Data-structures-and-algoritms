arr = []

for i in range(3):
    a = []
    for j in range(4):
        a.append(int(input()))
    arr.append(a)


for i in range(3):
    for j in range(4):
        print(arr[i][j], end=" ")
    print()