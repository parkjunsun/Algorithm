from itertools import product

n = int(input())
k = int(input())
cur = 100
numbers = [str(i) for i in range(10)]
if k != 0:
    arr = list(map(str, input().split()))
    for item in arr:
        if item in numbers:
            numbers.remove(item)

length = len(str(n))
candidates = list(product(numbers, repeat=length))
if length != 1:
    candidates.extend(list(product(numbers, repeat=length - 1)))
if length != 6:
    candidates.extend(list(product(numbers, repeat=length + 1)))

case1 = int(1e9)
max_channel = -1

for candidate in candidates:
    val = int(''.join(candidate))
    diff = abs(n - val)
    tmp = len(str(val)) + diff
    if tmp <= case1:
        case1 = tmp

case2 = abs(n - cur)

print(min(case1, case2))
