def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    part1 = [0] * n1
    part2 = [0] * n2

    for i in range(n1):
        part1[i] = arr[l + i]
    for j in range(n2):
        part2[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if part1[i] <= part2[j]:
            arr[k] = part1[i]
            i += 1
        else:
            arr[k] = part2[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = part1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = part2[j]
        j += 1
        k += 1

    
def mergeSort(arr, l, r):
    if l < r:
        m = (r + l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        

arr = list(map(int, input().split()))
print("Given array is:")
print(*arr)

l = 0
r = len(arr) - 1
mergeSort(arr, l, r)
print("Sorted array is:")
print(*arr)
