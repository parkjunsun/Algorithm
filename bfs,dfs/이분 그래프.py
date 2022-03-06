from collections import deque

def bfs(start, color):
    q = deque()
    q.append((start, color))
    colors[start] = color

    while q:
        start, color = q.popleft()
        for item in graph[start]:
            if not colors[item]:
                colors[item] = color * -1
                q.append((item, color * -1))
            elif colors[item] == colors[start]:
                return False

    return True

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    colors = [0] * (v+1)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        graph[i].sort()


    ans = False
    for i in range(1, v+1):
        if not colors[i]:
            if not bfs(i, 1):
                ans = True

    if ans:
        print("NO")
    else:
        print("YES")