class DiceCombinations:

    def dice(self, p, target):
        if target == 0:
            print(p)
            return

        for i in range(1, 7):
            if i <= target:
                self.dice(p + str(i), target - i)

    def dice_arr(self, p, target):
        l = []
        if target == 0:
            l.append(p)
            return l

        for i in range(1, 7):
            if i <= target:
                arr_list = self.dice_arr(p + str(i), target - i)
                map_arr = map(int, arr_list)
                l.extend(map_arr)
        return l

obj = DiceCombinations()
# obj.dice('', 4)
print(obj.dice_arr('', 4))
