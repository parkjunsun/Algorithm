from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

candidates = list(combinations(arr, 3))

ans = -int(1e9)
for candidate in candidates:
    if sum(candidate) <= m:
        ans = max(ans, sum(candidate))

print(ans)