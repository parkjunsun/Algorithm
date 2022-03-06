from itertools import combinations
from copy import deepcopy
import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input().split())))
empty = []
teachers = []
students = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            empty.append((i, j))
        elif board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'S':
            students += 1
candidates = list(combinations(empty, 3))

def init(candidate):
    res = deepcopy(board)
    for point in candidate:
        res[point[0]][point[1]] = 'O'
    return res

def check(teacher):
    x, y = teacher[0], teacher[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                break
            if hallway[nx][ny] == 'O':
                break
            if hallway[nx][ny] == 'S':
                hallway[nx][ny] = 'X'
            nx += dx[i]
            ny += dy[i]

flag = False

for candidate in candidates:
    hallway = init(candidate)
    check_cnt = 0
    for teacher in teachers:
        check(teacher)
    for i in range(n):
        for j in range(n):
            if hallway[i][j] == 'S':
                check_cnt += 1
    if students == check_cnt:
        print("YES")
        flag = True
        break

if not flag:
    print("NO")


