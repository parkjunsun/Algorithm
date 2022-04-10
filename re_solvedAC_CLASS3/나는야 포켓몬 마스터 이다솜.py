n, m = map(int, input().split())

dic1, dic2 = {}, {}

for i in range(n):
    name = input()
    dic1[name] = str(i+1)
    dic2[str(i+1)] = name

for _ in range(m):
    q = input()
    if q.isdigit():
        print(dic2[q])
    else:
        print(dic1[q])

