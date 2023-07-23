
def insert_at_bottom(stack, x):
    if len(stack) == 0:
        stack.append(x)
        return 
    
    temp = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(temp)




stack = [10 ,20, 30, 40, 50]
x = 321


insert_at_bottom(stack, x)
print(stack)