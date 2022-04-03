n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x: (x[1], x[0]))

for pos in arr:
    print(pos[0], pos[1])
