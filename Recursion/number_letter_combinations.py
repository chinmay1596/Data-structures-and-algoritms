class LetterCombinations:
    def pad(self, p, up):
        if len(up) == 0:
            print(p)
            return

        digit = int(up[0])

        for i in range((digit - 1) * 3, digit * 3):
            ch = chr(97 + i)
            self.pad(p + ch, up[1:])

    def pad_array(self, p, up, mapping):
        l = []
        if len(up) == 0:
            l.append(p)
            return l

        digit = int(up[0])
        value = mapping[digit]
        for i in range(len(value)):
            ch = value[i]
            comb = self.pad_array(p + ch, up[1:], mapping)
            new = l.extend(comb)
        return l

    def main(self, nums):
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return self.pad_array('', nums, mapping)


obj = LetterCombinations()
print(obj.main('23'))
