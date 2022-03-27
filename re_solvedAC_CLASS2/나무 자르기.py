n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
ans = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for item in arr:
        if item >= mid:
            total += (item - mid)

    if total >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
