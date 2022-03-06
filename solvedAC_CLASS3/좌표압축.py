n = int(input())
tmp = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append((tmp[i], i))

arr.sort()

a = [(arr[0][0], 0, arr[0][1])]
for i in range(1, n):
    if a[i-1][0] == arr[i][0]:
        a.append((arr[i][0], a[i-1][1], arr[i][1]))
    else:
        a.append((arr[i][0], a[i-1][1]+1, arr[i][1]))

a.sort(key=lambda x:x[2])
for item in a:
    print(item[1], end=' ')