t = int(input())
for _ in range(t):
    n = int(input())
    fashion = {}
    for _ in range(n):
        a, b = map(str, input().split())
        if b not in fashion:
            fashion[b] = 1
        else:
            fashion[b] += 1

    total = 1
    for key in fashion:
        total *= (fashion[key] + 1)

    ans = total - 1
    print(ans)
