n, m = map(int, input().split())
dic = {}

for _ in range(n):
    name = input()
    dic[name] = 1

for _ in range(m):
    name = input()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

arr = []
for key in dic:
    if dic[key] == 2:
        arr.append(key)

arr.sort()

print(len(arr))
for item in arr:
    print(item)

