n = int(input())
arr = []
for i in range(n):
    a, b = map(str, input().split())
    arr.append((a, b, i))

arr.sort(key=lambda x: (int(x[0]), x[2]))

for item in arr:
    print(item[0], item[1])
