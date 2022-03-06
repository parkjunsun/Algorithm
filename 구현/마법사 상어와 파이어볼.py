import sys
input = sys.stdin.readline


def restore(row, col):
    save[row][col][0] = 0
    save[row][col][1] = 0
    save[row][col][2] = 0


n, m, k = map(int, input().split())
save = [[[0] * 3 for _ in range(n)] for _ in range(n)]
pos = []

for _ in range(m):
    r, c, mass, s, d = map(int, input().split())
    pos.append((r-1, c-1, mass, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    tmp = [[[] for _ in range(n)] for _ in range(n)]
    for fireball in pos:
        x, y = fireball[0], fireball[1]
        weight = fireball[2]
        move = fireball[3]
        direction = fireball[4]

        nx = (move * dx[direction] + x) % n
        ny = (move * dy[direction] + y) % n

        save[nx][ny][0] += 1
        save[nx][ny][1] += weight
        save[nx][ny][2] += move
        tmp[nx][ny].append(direction)
    pos.clear()
    for i in range(n):
        for j in range(n):
            if save[i][j][0] >= 2:
                odd, even = 0, 0
                dm = save[i][j][1] // 5
                if dm == 0:
                    restore(i, j)
                    continue
                ds = save[i][j][2] // save[i][j][0]
                for num in tmp[i][j]:
                    if num % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                if odd == save[i][j][0] or even == save[i][j][0]:
                    for d in [0, 2, 4, 6]:
                        f = (i, j, dm, ds, d)
                        pos.append(f)
                else:
                    for d in [1, 3, 5, 7]:
                        f = (i, j ,dm, ds, d)
                        pos.append(f)
                restore(i, j)
            elif save[i][j][0] == 1:
                f = (i, j, save[i][j][1], save[i][j][2], tmp[i][j][0])
                pos.append(f)
                restore(i, j)
answer = 0
for item in pos:
    answer += item[2]

print(answer)