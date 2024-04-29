import math

def cut_rod(p, n):
    if len(p) < n:
        return None
    if n == 0:
        return 0
    q = -math.inf
    for i in range(n):
      q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q

def memoized_cut_rod(p, n):
    if len(p) < n:
        return None
    r = [-math.inf for x in range(n + 1)]
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = -math.inf
    if n == 0:
        q = 0
    else:
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    r[n] = q
    return q

def bottom_up_cut_rod(p, n):
    if len(p) < n:
        return None
    r = [0 for x in range(n + 1)]
    for i in range(1, n + 1):
        q = -math.inf
        for j in range(i):
            q = max(q, p[j] + r[i - j - 1])
        r[i] = q
    return r[n]


arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print("Please enter size of rod:")
n = int(input())
# res = cut_rod(arr, n)
# res = memoized_cut_rod(arr, n)
res = bottom_up_cut_rod(arr, n)
if res is None:
    print("Not enough prices for rod of len =", n)
else:
    print("Max income is", res) 
