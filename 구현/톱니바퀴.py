from collections import deque

q1 = deque(list(map(int, input())))
q2 = deque(list(map(int, input())))
q3 = deque(list(map(int, input())))
q4 = deque(list(map(int, input())))

arr = []
arr.append(q1)
arr.append(q2)
arr.append(q3)
arr.append(q4)

k = int(input())
for _ in range(k):
    cmds = []
    num, d = map(int, input().split())
    tmp_num = num - 1
    tmp_d = d
    num = num - 1
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

    num = tmp_num
    d = tmp_d

    while True:
        if num == 3:
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
gop = 1
for i in range(len(arr)):
    ans += arr[i][0] * gop
    gop *= 2

print(ans)



