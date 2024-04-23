# To heapify subtree rooted at index i.
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


#To build max heap
def buildMaxHeap(arr, n):
    # Since last parent will be at (n//2 - 1) we can start at that location
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)


def heapSort(arr):
    n = len(arr)
    buildMaxHeap(arr, n)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    
print("Given array is:")
arr = list(map(int, input().split()))
heapSort(arr)
print("Sorted array is:")
print(*arr)