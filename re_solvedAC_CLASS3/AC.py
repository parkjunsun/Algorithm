from collections import deque

t = int(input())
for _ in range(t):
    cmds = input()
    n = int(input())
    arr_str = input()

    cnt = cmds.count('D')
    if cnt > n:
        print("error")
        continue

    replace = cmds.replace("RR", "")
    arr = deque(arr_str[1:-1].split(','))
    flag = 0
    for char in replace:
        if char == 'R':
            flag += 1
        elif char == 'D' and flag % 2 == 1:
            arr.pop()
        elif char == 'D' and flag % 2 == 0:
            arr.popleft()

    if flag % 2 == 1:
        ans = '[' + ','.join(list(arr)[::-1]) + ']'
    else:
        ans = '[' + ','.join(arr) + ']'
    print(ans)

