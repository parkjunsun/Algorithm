n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b, 1])


for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    arr[i][2] += cnt


for item in arr:
    print(item[2], end=' ')
