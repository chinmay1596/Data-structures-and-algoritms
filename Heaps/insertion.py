class Heap:
    arr = [-1]

    @classmethod
    def insert(cls, val):
        cls.arr.append(val)
        index = len(cls.arr) - 1

        while index > 1:
            parent = index // 2
            if cls.arr[parent] < cls.arr[index]:
                cls.arr[parent], cls.arr[index] = cls.arr[index], cls.arr[parent]
                index = parent

            else:
                return

    @classmethod
    def print_heap(cls):
        for i in range(1, len(cls.arr)):
            print(cls.arr[i], end=' ')

    @classmethod
    def delete(cls):
        if len(cls.arr) == 1:
            return
        num = cls.arr.pop()
        cls.arr[1] = num

        index = 1
        while index < len(cls.arr):
            left_index = 2 * index
            right_index = 2 * index + 1

            if left_index < len(cls.arr) and cls.arr[index] < cls.arr[left_index]:
                cls.arr[index], cls.arr[left_index] = cls.arr[left_index], cls.arr[index]
                index = left_index

            elif right_index < len(cls.arr) and cls.arr[index] < cls.arr[right_index]:
                cls.arr[index], cls.arr[right_index] = cls.arr[right_index], cls.arr[index]
                index = right_index
            else:
                return


def heapify(arr, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and arr[largest] < arr[left]:
        largest = left

    if right <= n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, i)


def heap_sort(arr, n):
    size = n

    while size > 1:
        arr[1], arr[size] = arr[size], arr[1]
        size -= 1
        heapify(arr, size, 1)


obj = Heap()
obj.insert(50)
obj.insert(55)
obj.insert(53)
obj.insert(52)
obj.insert(54)
obj.print_heap()
obj.delete()
print()
obj.print_heap()
print()
print("printing heapify arr")
arr = [-1, 54, 53, 55, 52, 50]
n = len(arr) - 1

# heap creation
for i in range(n // 2, 0, -1):
    heapify(arr, n, i)

for i in range(1, len(arr)):
    print(arr[i], end=' ')

heap_sort(arr, n)
print()
print("Sorted Array:")
for i in range(1, len(arr)):
    print(arr[i], end=' ')