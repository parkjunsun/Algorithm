k, n = map(int, input().split())
arr = []
for _ in range(k):
    lan = int(input())
    arr.append(lan)

left = 1
right = max(arr)
result = -1

while left <= right:
    mid = (left + right) // 2
    total = 0

    for item in arr:
        share = item // mid
        total += share

    if total >= n:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)