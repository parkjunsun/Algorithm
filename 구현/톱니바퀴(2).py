from collections import deque

t = int(input())
arr = []
for _ in range(t):
    q = deque(list(map(int, input())))
    arr.append(q)

k = int(input())
for _ in range(k):
    num, d = map(int, input().split())
    num = num - 1
    tmp_num, tmp_d = num, d

    cmds = []
    cmds.append((num, d))

    while True:
        if num == 0:
            break
        if arr[num][-2] == arr[num-1][2]:
            break
        else:
            d = d * -1
            cmds.append((num-1, d))
            num -= 1

    num, d = tmp_num, tmp_d
    while True:
        if num == t-1:
            break
        if arr[num][2] == arr[num+1][-2]:
            break
        else:
            d = d * -1
            cmds.append((num+1, d))
            num += 1

    for cmd in cmds:
        arr[cmd[0]].rotate(cmd[1])

ans = 0
for i in range(len(arr)):
    if arr[i][0] == 1:
        ans += 1

print(ans)