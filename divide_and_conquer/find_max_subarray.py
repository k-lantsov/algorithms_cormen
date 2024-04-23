import math


def findMaxCrossingSubarray(arr, low, mid, high):

    left_sum = -math.inf
    sum = 0
    
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            min_left = i
    
    right_sum = -math.inf
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (min_left, max_right, left_sum + right_sum)


def findMaxSubarray(arr, low, high):

    if low == high:
        return (low, high, arr[low])
    else:
        mid = (high + low) // 2
        (left_low, left_high, left_sum) = findMaxSubarray(arr, low, mid)
        (right_low, right_hign, right_sum) = findMaxSubarray(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = findMaxCrossingSubarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_hign, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def bruteForceFindMaxSubarray(arr):

    max_sum = -math.inf
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum >= max_sum:
                max_sum = sum
                low = i
                high = j
    return (low, high, max_sum)


def linearFindMaxSubarray(arr):

    max_sum = -math.inf
    sum = 0
    current_low = 0
    
    for i in range(len(arr)):
        sum += arr[i]
        if sum >= max_sum:
            max_sum = sum
            low = current_low
            high = i
        if sum < 0:
            sum = 0
            current_low = i + 1
    return (low, high, max_sum)



print("Given array is:")
arr = list(map(int, input().split()))
# (min_left, max_right, sum) = findMaxSubarray(arr, 0, len(arr) - 1)
# (min_left, max_right, sum) = bruteForceFindMaxSubarray(arr)
(min_left, max_right, sum) = linearFindMaxSubarray(arr)
print("Max subarray is:")
print(*arr[min_left:max_right + 1])