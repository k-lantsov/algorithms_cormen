def add_binary(A, B):
    C = [0] * (len(A) + 1)
    carry = 0
    for i in range(len(A) - 1, -1 , -1):
        sum = A[i] + B[i] + carry
        C[i + 1] = sum % 2
        carry = sum // 2
    C[0] = carry
    return C

input_list1 = list(map(int, input().split()))
input_list2 = list(map(int, input().split()))
result = add_binary(input_list1, input_list2)
print(*result)