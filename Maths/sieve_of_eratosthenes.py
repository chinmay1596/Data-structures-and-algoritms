

class Sieve:
    def sieve_of_eratosthenes(self, arr, n):
        arr = arr * (n + 1)
        i = 2

        while i * i <= n:
            if not arr[i]:
                # mark all multiples of i to True
                # starting from i*2 because on i we are already there
                for j in range(i * 2, n + 1, i):
                    arr[j] = True
            i += 1
        return arr

    def print(self, arr, n):
        arr = self.sieve_of_eratosthenes(arr, n)
        for k in range(2, len(arr)):
            if not arr[k]:
                print(k, end=' ')


obj = Sieve()
obj.print([False], 20)
