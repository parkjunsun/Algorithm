n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

record = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            record[i] += 1

for num in record:
    print(num, end=' ')