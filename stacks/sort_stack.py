

def insert_element(stack, x):
    if len(stack) == 0:
        stack.append(x)
        return
    
    if stack[-1] >= x:
        stack.append(x)
        return
    temp = stack.pop()
    insert_element(stack, x)
    stack.append(temp)


def sort_stack(stack):
    if len(stack) == 0:
        return
    temp = stack.pop()
    sort_stack(stack)
    insert_element(stack, temp)


stack = [3, 2, 1]
sort_stack(stack)
print(stack)