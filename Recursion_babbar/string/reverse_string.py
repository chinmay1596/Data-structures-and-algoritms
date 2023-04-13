def reverse_string(s, i, j):
    if i >= j:
        return s
    s[i], s[j] = s[j], s[i]
    return reverse_string(s, i + 1, j - 1)


s = 'babbar'
print(''.join(reverse_string(list(s), 0, len(s) - 1)))


def reverse_string1(s, index, ans):
    if index < 0:
        return ans
    ans += s[index]
    return reverse_string1(s, index - 1, ans)


s = 'babbar'
ans = ''
print(reverse_string1(s, len(s) - 1, ans))
