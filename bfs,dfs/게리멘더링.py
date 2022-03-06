from collections import deque
from itertools import combinations
import sys

n = int(input())
districts = []

def division(num):
    num2 = len(districts) - num
    red = list(combinations(districts, num))
    blue = list(combinations(districts, num2))
    blue.reverse()
    return red, blue

popu = list(map(int, input().split()))
arr = []
for i in range(n):
    info = list(map(int, input().split()))
    districts.append(i+1)
    info.pop(0)
    arr.append(info)

if n == 2 and len(districts) == 0:
    print(abs(popu[0]-popu[1]))
    sys.exit()

graph = [[] for _ in range(n+1)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] not in graph[i+1]:
            graph[i+1].append(arr[i][j])
        if i+1 not in graph[arr[i][j]]:
            graph[arr[i][j]].append(i+1)

visited = [0] * (len(districts) + 1)
def division_check(start):
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

def red_bfs(init):
    if len(init) == 1:
        return 0
    for start in init:
        save = []
        q = deque()
        red_visited = [0] * (n + 1)
        q.append(start)
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not red_visited[i] and i in init:
                    q.append(i)
                    red_visited[i] = 1
                    save.append(i)
        save = list(set(save))
        if len(save) != len(init):
            return -1
    return 0


def blue_bfs(init):
    if len(init) == 1:
        return 0
    for start in init:
        save = []
        q = deque()
        blue_visited = [0] * (n+1)
        q.append(start)
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not blue_visited[i] and i in init:
                    q.append(i)
                    blue_visited[i] = 1
                    save.append(i)
        save = list(set(save))
        if len(save) != len(init):
            return -1
    return 0

di = 0
for number in districts:
    if visited[number] == 0:
        division_check(number)
        di += 1

if di == 0:
    print(-1)
    sys.exit()
if di > 2:
    print(-1)
    sys.exit()

min_diff = int(1e9)
for count in range(1, len(districts)):
    reds, blues = division(count)
    length = len(reds)
    mdiff = int(1e9)
    for i in range(length):
        red_flag = red_bfs(reds[i])
        blue_flag = blue_bfs(blues[i])
        rsums, bsums = 0, 0
        if red_flag == 0 and blue_flag == 0:
            for k in range(len(reds[i])):
                rsums += popu[reds[i][k]-1]
            for k in range(len(blues[i])):
                bsums += popu[blues[i][k]-1]
            diff = abs(rsums - bsums)
            mdiff = min(mdiff, diff)
    min_diff = min(min_diff, mdiff)

print(min_diff)
