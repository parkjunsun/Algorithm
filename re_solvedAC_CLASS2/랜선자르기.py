k, n = map(int, input().split())
arr = []
for _ in range(k):
    lan = int(input())
    arr.append(lan)

start, end = 1, max(arr)
ans = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for l in arr:
        cnt += l // mid

    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid
print(ans)