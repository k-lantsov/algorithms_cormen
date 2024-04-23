def bubble_sort(A):
    for i in range(len(A)):
        swapped = False
        for j in range(1, len(A) - i):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
                swapped = True
        if not swapped:
            break

arr = list(map(int, input().split()))
print("Given array is:")
print(*arr)

bubble_sort(arr)
print("Sorted array is:")
print(*arr)