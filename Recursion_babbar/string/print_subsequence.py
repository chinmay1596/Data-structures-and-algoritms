def subsequence(string, index, ans):
    if index == len(string):
        print(ans)
        return

    # include
    subsequence(string, index + 1, ans + string[index])

    # exclude
    subsequence(string, index + 1, ans)


# subsequence('abc', 0, '')


def subsequence1(string, index, ans, output):
    if index == len(string):
        output.append(ans)
        return output

    # include
    subsequence1(string, index + 1, ans + string[index], output)

    # exclude
    subsequence1(string, index + 1, ans, output)
    return output


output = []
print(subsequence1('abc', 0, '', output))
