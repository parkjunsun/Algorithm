n, s = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0

def recursive(depth, sums):
    global cnt

    if depth >= n:
        return

    sums += a[depth]
    print(sums)

    if sums == s:
        cnt += 1

    recursive(depth+1, sums - a[depth])
    recursive(depth+1, sums)


recursive(0, 0)
print(cnt)