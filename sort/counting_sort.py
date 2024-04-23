def countingSort(arr):
    output = [0] * len(arr)
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        output[count[arr[i]]] = arr[i]
    return output

print("Given array is:")
arr = list(map(int, input().split()))
ans = countingSort(arr)
print("Sorted array is:")
print(*ans)