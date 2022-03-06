from copy import deepcopy
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
mark = list(map(int, input().split()))
ops = []

plus, minus, mul, div = mark[0], mark[1], mark[2], mark[3]

def recursive(tmp, n):
    global plus, minus, mul, div
    if len(tmp) == n:
        ops.append(deepcopy(tmp))
        return

    if tmp.count('+') < plus:
        tmp.append('+')
        recursive(tmp, n)
        tmp.pop()

    if tmp.count('-') < minus:
        tmp.append('-')
        recursive(tmp, n)
        tmp.pop()

    if tmp.count('*') < mul:
        tmp.append('*')
        recursive(tmp, n)
        tmp.pop()

    if tmp.count('/') < div:
        tmp.append('/')
        recursive(tmp, n)
        tmp.pop()


recursive([], n-1)
print(ops)
min_ans = int(1e9)
max_ans = int(1e9) * -1

for i in range(len(ops)):
    ex = []
    for j in range(n-1):
        ex.append(nums[j])
        ex.append(ops[i][j])
    ex.append(nums[-1])
    ans = int(ex[0])

    for k in range(2, len(ex), 2):
        if ex[k-1] == '+':
            ans += int(ex[k])
        elif ex[k-1] == '-':
            ans -= int(ex[k])
        elif ex[k-1] == '*':
            ans *= int(ex[k])
        elif ex[k-1] == '/':
            if ans < 0:
                ans = -(abs(ans) // int(ex[k]))
            else:
                ans //= int(ex[k])

    min_ans = min(min_ans, ans)
    max_ans = max(max_ans, ans)

print(max_ans)
print(min_ans)


