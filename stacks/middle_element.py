

def middle_element(stack, total_size):
    if len(stack) == 0:
        print("No element in stack")
        return 
    
    if len(stack) == total_size // 2:
        print(stack[-1])
        return
    
    temp = stack.pop()
    middle_element(stack, total_size)
    stack.append(temp)

stack = [10, 20, 30, 40, 50, 60, 70]

middle_element(stack, len(stack))