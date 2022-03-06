import sys

input = sys.stdin.readline
n = int(input())
s = [0] * 21

for _ in range(n):
    cmds = sys.stdin.readline().rstrip().split()
    if cmds[0] == "add":
        if s[int(cmds[1])] == 0:
            s[int(cmds[1])] = 1
    elif cmds[0] == "remove":
        if s[int(cmds[1])] == 1:
            s[int(cmds[1])] = 0
    elif cmds[0] == "check":
        if s[int(cmds[1])] == 1:
            print(1)
        else:
            print(0)
    elif cmds[0] == "toggle":
        if s[int(cmds[1])] == 1:
            s[int(cmds[1])] = 0
        else:
            s[int(cmds[1])] = 1
    elif cmds[0] == "all":
        s = [1] * 21
    elif cmds[0] == "empty":
        s = [0] * 21

