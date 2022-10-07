class InPlaceMegeSort:

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        self.merge(left, right, arr)

    def merge(self, left, right, arr):
        len_left = len(left)
        len_right = len(right)
        i = j = k = 0

        while i < len_left and j < len_right:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len_left:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len_right:
            arr[k] = right[j]
            j += 1
            k += 1


a = InPlaceMegeSort()
arr = [10, 10]
a.merge_sort(arr)
print(arr)
