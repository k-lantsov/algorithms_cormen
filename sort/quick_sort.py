import random

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

def quickSort(arr, p, r):
    if p < r:
        q = randomizedPartition(arr, p, r)
        quickSort(arr, p, q - 1)
        quickSort(arr, q + 1, r)

print("Given array is:")
arr = list(map(int, input().split()))
quickSort(arr, 0, len(arr) - 1)
print("Sorted array is:")
print(*arr)