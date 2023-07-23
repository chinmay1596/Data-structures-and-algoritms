def skipa(s, index):
    ans = ''
    if index == len(s):
        return ans
    if s[index] != 'a':
        ans += s[index]
    belowcalls =  skipa(s, index + 1)
    ans+=belowcalls
    return ans

# s = 'baccad'
# print(skipa(s, 0))


def skipapple(s, index, ans=''):

    if index == len(s):
        return ans
    if s[index:].startswith('apple'):
        return skipapple(s, index+5, ans)
    else:
        ans+=s[index]
        return skipapple(s, index+1, ans)

# s = 'applebcdapplefgapple'
# print(skipapple(s, 0))


def skipappnotapple(s, index, ans=''):

    if index == len(s):
        return ans
    if s[index:].startswith('app') and not s[index:].startswith('apple'):
        return skipappnotapple(s, index+3, ans)
    else:
        ans+=s[index]
        return skipappnotapple(s, index+1, ans)

s = 'applbcdapplfgapple'
print(skipappnotapple(s, 0))


