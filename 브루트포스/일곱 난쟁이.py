from itertools import combinations

arr = []
for _ in range(9):
    n = int(input())
    arr.append(n)

comb = list(combinations(arr, 7))
ans = []

for c in comb:
    if sum(c) == 100:
        for num in c:
            ans.append(num)
        break

ans.sort()
for x in ans:
    print(x)