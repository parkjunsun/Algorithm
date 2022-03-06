from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def bfs(x, depth):
    q = deque()
    q.append((x, depth))
    visited[x] = 1

    while q:
        import sys

        n, m = map(int, input().split())
        a = []
        b = []
        for _ in range(n):
            a.append(list(map(int, input())))
        for _ in range(n):
            b.append(list(map(int, input())))

        if n < 3 or m < 3:
            for i in range(n):
                for j in range(m):
                    if a[i][j] != b[i][j]:
                        print(-1)
                        sys.exit()

            print(0)
            sys.exit()

        cnt = 0
        breaker = False
        for i in range(n - 3 + 1):
            for j in range(m - 3 + 1):
                flag = False
                if a[i][j] != b[i][j]:
                    for x in range(3):
                        for y in range(3):
                            if a[x + i][y + j] == 0:
                                a[x + i][y + j] = 1
                            else:
                                a[x + i][y + j] = 0
                    cnt += 1

                for k in range(n):
                    for z in range(m):
                        if a[k][z] != b[k][z]:
                            flag = True

                if not flag:
                    breaker = True
                    break
            if breaker:
                break

        if breaker:
            print(cnt)
        else:
            print(-1)

