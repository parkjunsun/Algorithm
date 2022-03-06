n, m = map(int, input().split())

dic = {}
res = []

for _ in range(n):
    name = input()
    if name not in dic:
        dic[name] = 0

for _ in range(m):
    name = input()
    if name in dic:
        dic[name] += 1

for key in dic:
    if dic[key] >= 1:
        res.append(key)
res.sort()

print(len(res))
for name in res:
    print(name)