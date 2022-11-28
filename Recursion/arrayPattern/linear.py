target = 1


class LinearSearch:

    def linear_search(self, arr, index):
        """
        Simple linear search with recursion
        :param arr:
        :param index:
        :return:
        """
        if index == len(arr):
            return 'Not found'
        if arr[index] == target:
            return index
        return self.linear_search(arr, index + 1)

    def linear_search1(self, arr, index, l=[]):
        """
        Linear search with multiple answers
        :param arr:
        :param index:
        :param l:
        :return:
        """

        if index == len(arr):
            return l
        if arr[index] == target:
            l.append(index)
        return self.linear_search1(arr, index + 1, l)

    def linear_search2(self, arr, index):
        l = []
        if index == len(arr):
            return l
        if arr[index] == target:
            l.append(index)
        ans_from_below_calls = self.linear_search2(arr, index + 1)
        l.extend(ans_from_below_calls)
        return l


arr = [3, 2, 1, 1]
a = LinearSearch()
print(a.linear_search1(arr, 0))
