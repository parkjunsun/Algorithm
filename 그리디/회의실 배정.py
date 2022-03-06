n = int(input())
arr = []
for _ in range(n):
    s, f = map(int, input().split())
    arr.append((s, f))

arr.sort(key=lambda x:(x[1], x[0]))
total = 1

start = arr[0][0]
finish = arr[0][1]
arr.pop(0)

for item in arr:
    if item[0] >= finish:
        total += 1
        finish = item[1]

print(total)


