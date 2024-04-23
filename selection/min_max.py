def findMinMax(arr):
    max, min = 0, 0
    i = 0
    n = len(arr)

    if n % 2 != 0:
        min = arr[0]
        max = arr[0]
        i = 1
    else:
        if arr[0] < arr[1]:
            min = arr[0]
            max = arr[1]
        else:
            min = arr[1]
            max = arr[0]
        i = 2
    
    while i < n:
        if arr[i] < arr[i + 1]:
            if arr[i] < min:
                min = arr[i]
            if arr[i + 1] > max:
                max = arr[i + 1]
        else:
            if arr[i + 1] < min:
                min = arr[i + 1]
            if arr[i] > max:
                max = arr[i]
        i += 2
    return [max, min]

print("Given array is:")
arr = list(map(int, input().split()))
maxMin = findMinMax(arr)
print("MaxMin are:")
print(*maxMin)
