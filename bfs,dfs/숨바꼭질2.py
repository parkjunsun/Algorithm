from collections import deque

n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]

def bfs(x):
    q = deque()
    q.append(x)
    visited[x][0] = 0
    visited[x][1] = 1

    while q:
        x = q.popleft()
        for nx in (x+1, x-1, 2*x):
            if 0 <= nx <= 100000:
                if visited[nx][0] == -1:
                    visited[nx][0] = visited[x][0] + 1
                    visited[nx][1] = visited[x][1]
                    q.append(nx)
                elif visited[nx][0] == visited[x][0] + 1:  # 하나 차이가 나야지(= 같은 레벨)만 최단 거리 방법을 찾을 수 있다.
                    visited[nx][1] += visited[x][1]


bfs(n)
print(visited[k][0])
print(visited[k][1])
