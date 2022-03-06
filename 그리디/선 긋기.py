n = int(input())
import sys

input = sys.stdin.readline

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x:x[0])
start = arr[0][0]
end = arr[0][1]

ans = 0

for i in range(1, len(arr)):
    if arr[i][0] <= end:
        end = max(end, arr[i][1])
    else:
        ans += end - start
        start = arr[i][0]
        end = arr[i][1]

ans += end - start
print(ans)



