n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[1], x[0]))

start, finish = arr[0][0], arr[0][1]

cnt = 1
for i in range(1, len(arr)):
    if finish <= arr[i][0]:
        finish = arr[i][1]
        cnt += 1

print(cnt)