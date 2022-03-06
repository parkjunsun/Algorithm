n = int(input())
tmp = list(map(int, input().split()))

arr = []
for i in range(n):
    t = [tmp[i], i]
    arr.append(t)

arr.sort(key=lambda x:x[0])

cnt = 0
for i in range(n-1):
    arr[i].append(cnt)
    if arr[i][0] != arr[i+1][0]:
        cnt += 1

arr[n-1].append(cnt)
arr.sort(key=lambda x:x[1])

for i in range(n):
    print(arr[i][2], end=' ')