from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
operation = list(map(int, input().split()))

op = ['+'] * operation[0] + ['-'] * operation[1] + ['*'] * operation[2] + ['//'] * operation[3]
candidates = list(set(permutations(op)))

max_num = int(-1e9)
min_num = int(1e9)

for candidate in candidates:
    res = []
    for i in range(len(nums)):
        res.append(nums[i])
        if i >= len(candidate):
            break
        res.append(candidate[i])
    result = res[0]
    for i in range(1, len(res)-1, 2):
        if res[i] == '+':
            result += res[i+1]
        elif res[i] == '-':
            result -= res[i+1]
        elif res[i] == '*':
            result *= res[i+1]
        else:
            if result < 0:
                result = -(abs(result) // res[i+1])
            else:
                result //= res[i+1]
    max_num = max(result, max_num)
    min_num = min(result, min_num)

print(max_num)
print(min_num)

