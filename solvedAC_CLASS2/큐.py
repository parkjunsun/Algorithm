from collections import deque
import sys

n = int(input())
q = deque()

for _ in range(n):
    cmds = sys.stdin.readline().rstrip().split()
    if cmds[0] == "push":
        q.append(cmds[1])
    elif cmds[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmds[0] == "size":
        print(len(q))
    elif cmds[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmds[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmds[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])