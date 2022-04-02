import sys

n = int(input())
stack = []
for _ in range(n):
    cmds = sys.stdin.readline().rstrip().split()
    if len(cmds) > 1:
        cmd, num = cmds[0], cmds[1]
    else:
        cmd = cmds[0]

    if cmd == "push":
        stack.append(num)
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


