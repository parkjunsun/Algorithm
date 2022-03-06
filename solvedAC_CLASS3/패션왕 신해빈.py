t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}

    for _ in range(n):
        info = input().split()
        wear, part = info[0], info[1]
        if part not in dic:
            dic[part] = 2
        else:
            dic[part] += 1

    ans = 1
    for key in dic:
        ans *= dic[key]

    print(ans-1)