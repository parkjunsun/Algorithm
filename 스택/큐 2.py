from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    s = input()
    command = s.split()
    if len(command) == 2:
        cmd, num = command[0], command[1]
        if cmd == "push":
            q.append(num)
    else:
        cmd = command[0]
        if cmd == "pop":
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif cmd == "size":
            print(len(q))
        elif cmd == "empty":
            if q:
                print(0)
            else:
                print(1)
        elif cmd == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif cmd == "back":
            if q:
                print(q[-1])
            else:
                print(-1)




