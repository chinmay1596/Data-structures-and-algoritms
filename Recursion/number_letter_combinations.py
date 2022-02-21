
class LetterCombinations:
    def pad(self, p, up):
        if len(up) == 0:
            print(p)
            return

        digit = int(up[0])

        for i in range((digit-1)*3, digit*3):
            ch = chr(97+i)
            self.pad(p+ch, up[1:])

    def pad_array(self, p, up):
        l = []
        if len(up) == 0:
            l.append(p)
            return l

        digit = int(up[0])

        for i in range((digit - 1) * 3, digit * 3):
            ch = chr(97 + i)
            comb = self.pad_array(p + ch, up[1:])
            new = l.extend(comb)
        return l


obj = LetterCombinations()
print(obj.pad_array('', '12'))