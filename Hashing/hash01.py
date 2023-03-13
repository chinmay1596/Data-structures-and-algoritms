class HashMap:

    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t = HashMap()
t['march 1'] = 30
t['march 6'] = 33
t['march 8'] = 28
t['march 9'] = 34
t['march 17'] = 45
t['march 18'] = 46
t['march 104'] = 302

del t['march 18']
del t['march 104']
print("before", len(t.arr))
del t['march 1']
print(t.arr)
print("after", len(t.arr))


