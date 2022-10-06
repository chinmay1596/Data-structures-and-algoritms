def wavePrint(arr):
    l = []
    m = []
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            if i < len(arr) and j % 2 == 0:
                l.append(arr[i][j])
            else:
                if i < len(arr):
                    m.append(arr[i][j])
        m.reverse()
        l.extend(m)
        m.clear()
    return l


arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]
print(wavePrint(arr))
