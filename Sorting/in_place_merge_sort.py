class InPlaceMegeSort:

    def merge_sort(self, arr, low, high):
        if low >= high:
            return
        mid = (high + low) // 2
        self.merge_sort(arr, low, mid)
        self.merge_sort(arr, mid+1, high)
        self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        temp = []
        i = low
        j =  mid+1

        while i <= mid and j <= high:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= high:
            temp.append(arr[j])
            j += 1
        
        for k in range(low, high+1):
            arr[k] = temp[k-low]


a = InPlaceMegeSort()
arr = [5, 4, 3, 2, 1]
low = 0
high = len(arr)-1
a.merge_sort(arr, low, high)
print(arr)
