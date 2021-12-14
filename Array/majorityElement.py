"""
It is also called Moore's Voting algorithm
majority element is when element comes more than n/2 times where n is length of array
Time complexity: O(n)
"""


def majorityElement(arr):
    """
    Function to find the candidate for Majority
    :param arr:
    :return:
    """
    maj_index = 0
    count = 1

    for i in range(len(arr)):
        if arr[maj_index] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return arr[maj_index]


def isMajority(arr, cand):
    """
    Function to check if the candidate occurs more than n/2 times
    :param arr:
    :param cand:
    :return:
    """
    count = 0
    for i in range(len(arr)):
        if arr[i] == cand:
            count += 1

    if count > len(arr) // 2:
        return True
    else:
        return False


def majority(arr):
    cand = majorityElement(arr)
    if isMajority(arr, cand):
        return cand
    else:
        return "No Majority element Found"


arr = list(map(int, input("Enter elements:")))
print(majority(arr))
