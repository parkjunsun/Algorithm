from collections import deque
import sys

input = sys.stdin.readline

s, t = map(int, input().split())
if s == t:
    print(0)
    sys.exit()


visited = set()

def bfs(s, op):
    q = deque()
    q.append((s, op))
    visited.add(s)
    while q:
        s, op = q.popleft()
        if s == t:
            return op

        ns = s * s
        if 0 <= ns <= 10e9:
            if ns not in visited:
                q.append((ns, op + '*'))
                visited.add(ns)

        ns = s + s
        if 0 <= ns <= 10e9:
            if ns not in visited:
                q.append((ns, op + '+'))
                visited.add(ns)

        ns = s // s
        if ns not in visited:
            q.append((ns, op + '/'))
            visited.add(ns)

    return -1
print(bfs(s, ""))
