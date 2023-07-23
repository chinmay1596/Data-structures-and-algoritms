def reverse_string(s:str):
    stack = []
    ans = ""
    for i in s:
        stack.append(i)
    
    j = len(stack)-1
    while j >= 0:
        ans+=stack[j]
        j-=1
    return ans


print(reverse_string("abcd"))
