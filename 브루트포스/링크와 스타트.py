from itertools import combinations
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

arr = [i for i in range(1, n+1)]
c = list(combinations(arr, n//2))

min_num = int(1e9)

for i in range(len(c)//2):
    sTeam = 0
    lTeam = 0
    link = (len(c) - 1) - i
    s = list(c[i])
    sc = list(permutations(s, 2))
    for j in range(len(sc)):
        sTeam += board[sc[j][0]-1][sc[j][1]-1]

    l = list(c[link])
    lc = list(permutations(l, 2))
    for j in range(len(lc)):
        lTeam += board[lc[j][0]-1][lc[j][1]-1]

    min_num = min(min_num, abs(sTeam-lTeam))

print(min_num)