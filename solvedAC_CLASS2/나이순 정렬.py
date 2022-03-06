n = int(input())
arr = []
for i in range(n):
    old, name = map(str, input().split())
    arr.append((int(old), name, i))

arr.sort(key=lambda x:(x[0], x[2]))

for item in arr:
    print(item[0], item[1])