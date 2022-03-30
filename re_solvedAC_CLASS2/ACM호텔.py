t = int(input())
for _ in range(t):
    n, m, room = map(int, input().split())

    board = [[0] * (m+1) for _ in range(n+1)]
    cnt = 0
    ans = 0
    for i in range(1, m+1):
        breaker = False
        for j in range(n, 0, -1):
            cnt += 1
            if len(str(i)) == 1:
                tmp = '0' + str(i)
            else:
                tmp = str(i)
            board[j][i] = int(str((n+1) - j) + tmp)
            if cnt == room:
                ans = board[j][i]
                breaker = True
                break

        if breaker:
            break

    print(ans)