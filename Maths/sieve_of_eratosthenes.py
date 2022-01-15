

def sieve_of_eratosthenes(arr, n):
    arr = arr*(n+1)
    i = 2
    while i*i <= n:
        if arr[i]:
            for j in range(i*2, n+1, i):
                arr[j] = False
        i+=1
    for k in range(2, len(arr)):
        if arr[k]:
            print(k, end=' ')


sieve_of_eratosthenes([True], 37)