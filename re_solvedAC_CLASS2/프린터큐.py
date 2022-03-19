from collections import deque


def check(my, queue):
    if max(queue)[0] == my:
        return True
    else:
        return False


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    p = deque()

    for i in range(len(arr)):
        p.append((arr[i], i))

    ans = []
    while True:
        if len(p) == 0:
            break
        if check(p[0][0], p):
            ans.append(p.popleft())
        else:
            p.append(p.popleft())

    for i in range(len(ans)):
        if ans[i][1] == m:
            print(i+1)
            break
