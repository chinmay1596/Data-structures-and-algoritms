from copy import copy, deepcopy


class Subset:
    sub = [1, 2, 3]
    sub1 = [1, 2, 2]

    @classmethod
    def subset_array(cls):
        arr = []
        arr.append([])
        for i in cls.sub:
            internal_array = deepcopy(arr)
            for j in range(len(internal_array)):
                internal_array[j].append(i)
            arr.extend(internal_array)

        return arr

    def duplicate_subset(self):
        Subset.sub1.sort()
        arr = []
        arr.append([])
        start = 0
        end = 0
        for i in range(len(Subset.sub1)):
            internal_array = deepcopy(arr)
            if i > 0 and Subset.sub1[i] == Subset.sub1[i-1]:
                start = end+1
                end = len(arr)-1
            else:
                end = len(arr)-1
            for j in range(start, end+1):
                internal_array[j].append(Subset.sub1[i])
            arr.extend(internal_array[start:end+1])
        return arr

obj = Subset()
print(obj.duplicate_subset())