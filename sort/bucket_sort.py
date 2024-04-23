import insertion_sort as insertion

def bucketSort(arr):
    # Create buckets list
    buckets = []
    for i in range(len(arr)):
        buckets.append([])

    # Put elements of input array in different buckets
    for elem in arr:
        bucket_index = elem // len(arr)
        buckets[bucket_index].append(elem)
    
    # Sort individual buckets
    for elem in buckets:
        insertion.insertionSort(elem)
    
    # concatenate the result
    k = 0
    for i in range(len(arr)):
        bucket = buckets[i]
        while len(bucket) > 0:
            arr[k] = bucket[0]
            bucket.pop(0)
            k += 1
    return arr

print("Given array is:")
arr = list(map(int, input().split()))
ans = bucketSort(arr)
print("Sorted array is:")
print(*ans)