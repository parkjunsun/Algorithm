from collections import deque

n, k = map(int, input().split())
dist = [0] * 100001
visited = [0] * 100001
move = [0] * 100001

def trace(x):
    arr = [x]
    tmp = x
    for _ in range(dist[x]):
        tmp = move[tmp]
        arr.append(tmp)
    print(' '.join(map(str, arr[::-1])))

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            trace(x)
            return x
        for nx in (x - 1, x + 1, 2 * x):
            if -1 < nx < 100001:
                if visited[nx] == 0:
                    move[nx] = x
                    dist[nx] = dist[x] + 1
                    visited[nx] = 1
                    q.append(nx)
bfs(n)

