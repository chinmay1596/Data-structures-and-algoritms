

def insert_at_bottom(stack, x):
    if len(stack) == 0:
        stack.append(x)
        return 
    
    temp = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(temp)



def reverse_stack(stack):
    if len(stack) == 0:
        return
    
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)

stack = [10, 20, 30, 40, 50]
reverse_stack(stack)
print(stack)
