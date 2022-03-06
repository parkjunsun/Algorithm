from collections import deque
import math

sosu = [True] * 10005
sosu[0], sosu[1] = False, False

for i in range(2, int(math.sqrt(10000))+1):
    if sosu[i]:
        gop = 2
        while i*gop <= 10001:
            sosu[i*gop] = False
            gop += 1

def bfs(x, depth):
    q = deque()
    q.append((x, depth))
    visited[int(x)] = 1

    while q:
        x, depth = q.popleft()
        if x == m:
            return depth

        for i in range(0, 10):
            number = int(x[:3] + str(i))
            if sosu[number] and visited[number] == 0:
                visited[number] = 1
                q.append((str(number), depth+1))

        for i in range(0, 10):
            number = int(x[:2] + str(i) + x[-1])
            if sosu[number] and visited[number] == 0:
                visited[number] = 1
                q.append((str(number), depth+1))

        for i in range(0, 10):
            number = int(x[0] + str(i) + x[2:4])
            if sosu[number] and visited[number] == 0:
                visited[number] = 1
                q.append((str(number), depth+1))

        for i in range(1, 10):
            number = int(str(i) + x[1:4])
            if sosu[number] and visited[number] == 0:
                visited[number] = 1
                q.append((str(number), depth+1))

    return -1


t = int(input())
for _ in range(t):
    n, m = map(str, input().split())
    visited = [0] * 10001

    res = bfs(n, 0)
    if res == -1:
        print("Impossible")
    else:
        print(res)
