nums = [0, 4, 3, 0, 4]

#
# def fun():
#     nums.sort()
#     for i in range(len(nums)):
#         n = len(nums) - i
#         cond1 = n <= nums[i]
#         cond2 = (i - 1 < 0) or (n > nums[i - 1])
#         if cond1 and cond2:
#             return n
#     return -1
#
#
# print(fun())

grid = [[5, 1, 0], [-5, -5, -5]]


def fun(grid):
    count = 0
    row = 0
    col = 0

    while row <= len(grid) - 1 and col <= len(grid[0]) - 1:
        if grid[row][col] < 0:
            count += len(grid[0]) - col
            row += 1
            col = 0
        else:
            if col < len(grid[0])-1:
                col += 1
            else:
                row+=1
                col = 0
    return count


print(fun(grid))
