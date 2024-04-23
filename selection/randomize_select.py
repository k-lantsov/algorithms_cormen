import random

# split arr into 2 sorted parts and return index of pivot element of arr
def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def randomizedPartition(arr, p, r):
    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


# return ith elem of sorted arr
def randomizedSelect(arr, p, r, i):
    if p == r:
        return arr[p]
    q = randomizedPartition(arr, p, r)
    k = q - p
    if i == k:
        return arr[q]
    elif i < k:
        return randomizedSelect(arr, p, q - 1, i)
    else:
        return randomizedSelect(arr, q + 1, r, i - k)
    
print("given array is:")
arr = list(map(int, input().split()))
i = random.randint(0, len(arr) - 1)
print("random index is:")
print(i)
elem = randomizedSelect(arr, 0, len(arr) - 1, i)
print("ith elem of array is:")
print(elem)