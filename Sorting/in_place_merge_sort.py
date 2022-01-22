class InPlaceMegeSort:

    def merge_sort(self, arr, start, end):
        if end - start == 1:
            return

        mid = (end + start) // 2

        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid, end)

        self.merge(arr, start, mid, end)

    def merge(self, arr, start, mid, end):
        new_arr = [0] * (end - start)

        i = start
        j = mid
        k = 0

        while i < mid and j < end:
            if arr[i] < arr[j]:
                new_arr[k] = arr[i]
                i += 1
            else:
                new_arr[k] = arr[j]
                j += 1
            k += 1

        while i < mid:
            new_arr[k] = arr[i]
            i += 1
            k += 1

        while j < end:
            new_arr[k] = arr[j]
            j += 1
            k += 1

        for l in range(len(new_arr)):
            arr[start+l] = new_arr[l]


a = InPlaceMegeSort()
arr = [5, 4, 3, 2, 1]
a.merge_sort(arr, 0, len(arr))
print(arr)