def lcs(a: str, b: str, i: int, j: int):
    # base case
    if i == len(a):
        return 0
    if j == len(b):
        return 0

    # match
    ans = 0
    if a[i] == b[j]:
        ans = 1 + lcs(a, b, i + 1, j + 1)
    else:
        ans = max(lcs(a, b, i + 1, j), lcs(a, b, i, j + 1))
    return ans


a = "abcde"
b = "ace"
i = 0
j = 0
print(lcs(a, b, i, j))
