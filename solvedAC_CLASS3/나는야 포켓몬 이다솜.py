n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    name = input()
    dic[name] = str(i)
    dic[str(i)] = name

for _ in range(m):
    ans = input()
    print(dic[ans])