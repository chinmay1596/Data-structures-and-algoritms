def permutations(s, index):
    if index == len(s):
        print(''.join(s))
        return

    for j in range(index, len(s)):
        s[index], s[j] = s[j], s[index]
        permutations(s, index + 1)
        s[index], s[j] = s[j], s[index]


s = list('abc')
permutations(s, 0)
