from collections import deque
import sys

n = int(input())
q = deque()
for _ in range(n):
    cmds = sys.stdin.readline().rstrip().split()
    if len(cmds) > 1:
        cmd, num = cmds[0], cmds[1]
    else:
        cmd = cmds[0]

    if cmd == "push_front":
        q.appendleft(num)
    elif cmd == "push_back":
        q.append(num)
    elif cmd == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])

