n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

min_num = float('inf')
right = 0

for left in range(n):
    while right < n and arr[right] - arr[left] < m:
        right += 1
    if right == n:
        break
    min_num = min(min_num, arr[right] - arr[left])

print(min_num)

