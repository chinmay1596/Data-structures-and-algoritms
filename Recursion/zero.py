
global count
count = 0
def zero_number(n):
    if n == 0:
        return 1
    rem = n % 10
    if rem == 0:
        global count
        count+=1
    zero_number(n//10)
    return count
print(zero_number(1000))

def zero():
    pass