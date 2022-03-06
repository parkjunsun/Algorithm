n, c = map(int, input().split())
arr = []
for _ in range(n):
    home = int(input())
    arr.append(home)
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    cnt = 1
    mid = (start + end) // 2
    value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] >= value + mid:
            value = arr[i]
            cnt += 1
    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)