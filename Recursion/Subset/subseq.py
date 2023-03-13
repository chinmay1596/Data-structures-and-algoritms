
class SubSequence:

    def subseq(self, p, up):
        if len(up) == 0:
            print(p)
            return

        first_char = up[0]
        self.subseq(p+first_char, up[1:])
        self.subseq(p, up[1:])

    def subseq_array(self, p, up):
        l = []
        if len(up) == 0:
            l.append(p)
            return l

        first_char = up[0]

        a = self.subseq_array(p+first_char, up[1:])
        b = self.subseq_array(p, up[1:])
        a.extend(b)
        return a

    def subseq_array1(self, p, up, l=[]):
        if len(up) == 0:
            l.append(p)
            return l
        first_char = up[0]

        self.subseq_array1(p + first_char, up[1:])
        self.subseq_array1(p, up[1:])
        return l

ob = SubSequence()
print(ob.subseq_array(' ', 'aba'))

