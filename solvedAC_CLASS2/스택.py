import sys

n = int(input())
stack = []

for _ in range(n):
    cmds = sys.stdin.readline()
    cmds = cmds.split(' ')
    if cmds[0] == "push":
        number = cmds[1].strip()
        stack.append(number)
    elif cmds[0].strip() == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmds[0].strip() == "size":
        print(len(stack))
    elif cmds[0].strip() == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmds[0].strip() == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
