class InversionCount:

    def mergeSort(self, arr):
        return self.merge_sort(arr, 0, len(arr))

    def merge_sort(self, arr, start, end):
        inversion_count = 0
        if end - start == 1:
            return

        mid = (end + start) // 2

        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid, end)

        inversion_count += self.merge(arr, start, mid, end)
        return inversion_count

    def merge(self, arr, start, mid, end):
        new_arr = [0] * (end - start)
        inversion_count = 0
        i = start
        j = mid
        k = 0

        while i < mid and j < end:
            if arr[i] < arr[j]:
                new_arr[k] = arr[i]
                i += 1
            else:
                new_arr[k] = arr[j]
                inversion_count += (mid-i +1)
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
            arr[start + l] = new_arr[l]
        return inversion_count


arr = [2, 4, 1, 3, 5]
obj = InversionCount()
print(obj.mergeSort(arr))



