from itertools import product
from copy import deepcopy

# def recursive(tmp, n):
#     if len(tmp) == n:
#         ops.append(deepcopy(tmp))
#         return
#
#     tmp.append(' ')
#     recursive(tmp, n)
#     tmp.pop()
#
#     tmp.append('+')
#     recursive(tmp, n)
#     tmp.pop()
#
#     tmp.append('-')
#     recursive(tmp, n)
#     tmp.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [str(i) for i in range(1, n+1)]
    mark = ['+', '-', ' ']
    ops = list(product(mark, repeat=n-1))
    # recursive([], n-1)
    arr = []

    for i in range(len(ops)):
        ex = ""
        for j in range(n-1):
            ex += numbers[j] + ops[i][j]
        ex += numbers[-1]
        tmp = ex.replace(' ', '')
        if eval(tmp) == 0:
            arr.append(ex)

    arr.sort()
    for res in arr:
        print(res)
    print()