def defaultSquareMatrixMultiply(matrix1, matrix2): 
    n = len(matrix1)
    ans = [[0 for x in range(n)] for y in range(n)] 
    for i in range(n):
        for j in range(n):
            ans[i][j] = 0
            for k in range(n):
                ans[i][j] += matrix1[i][k] * matrix2[k][j]
    return ans

def splitMatrix(matrix, n):
    top_left = []
    top_right = []
    bot_left = []
    bot_right = []
    for i in range(n):
        top_left_i = []
        top_right_i = []
        bot_left_i = []
        bot_right_i = []
        for j in range(n):
            top_left_i.append(matrix[i][j])
            top_right_i.append(matrix[i][j+n])
            bot_left_i.append(matrix[i+n][j])
            bot_right_i.append(matrix[i+n][j+n])
        top_left.append(top_left_i)
        top_right.append(top_right_i)
        bot_left.append(bot_left_i)
        bot_right.append(bot_right_i)
    return top_left, top_right, bot_left, bot_right

def addMatrix(m1, m2, n):
    res = [[0 for i in range(n)] for j in range(n)] 
    for i in range(n):
        for j in range(n):
            res[i][j] = m1[i][j] + m2[i][j]
    return res

def collectMatrix(m_11, m_12, m_21, m_22, n):
    res = [[0 for x in range(n)] for y in range(n)]
    for i in range(n//2):
        for j in range(n//2):
            res[i][j] = m_11[i][j]
            res[i][j+n//2] = m_12[i][j]
            res[i+n//2][j] = m_21[i][j]
            res[i+n//2][j+n//2] = m_22[i][j]
    return res

def squareMatrixMultiplyRecursive(m1, m2):    
    n = len(m1)
    if n == 2:
        return defaultSquareMatrixMultiply(m1, m2)
    split_index = n//2
    m1_11, m1_12, m1_21, m1_22 = splitMatrix(m1, split_index)
    m2_11, m2_12, m2_21, m2_22 = splitMatrix(m2, split_index)
    m_11 = addMatrix(squareMatrixMultiplyRecursive(m1_11, m2_11), squareMatrixMultiplyRecursive(m1_12, m2_21), split_index)
    m_12 = addMatrix(squareMatrixMultiplyRecursive(m1_11, m2_12), squareMatrixMultiplyRecursive(m1_12, m2_22), split_index)
    m_21 = addMatrix(squareMatrixMultiplyRecursive(m1_21, m2_11), squareMatrixMultiplyRecursive(m1_22, m2_21), split_index)
    m_22 = addMatrix(squareMatrixMultiplyRecursive(m1_21, m2_12), squareMatrixMultiplyRecursive(m1_22, m2_22), split_index)
    res = collectMatrix(m_11, m_12, m_21, m_22, n)
    return res

print("Enter square matrices dimension:")
n = int(input())
matrix1 = [[0 for x in range(n)] for y in range(n)]
matrix2 = [[0 for x in range(n)] for y in range(n)]
print("Enter matrix #1 rows:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix1[i] = row
print("Enter matrix #2 rows:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix2[i] = row

# res = defaultSquareMatrixMultiply(matrix1, matrix2)
res = squareMatrixMultiplyRecursive(matrix1, matrix2)
print(*res)