import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)
result = -1

while left <= right:
    mid = (left + right) // 2
    total = 0

    for item in arr:
        remain = item - mid
        if remain < 0:
            remain = 0
        total += remain

    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
