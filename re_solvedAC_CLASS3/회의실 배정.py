n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

end = arr[0][1]
cnt = 1

for i in range(1, len(arr)):
    s, e = arr[i][0], arr[i][1]
    if end <= s:
        cnt += 1
        end = e

print(cnt)
