from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    priority = []
    for i in range(len(tmp)):
        priority.append((tmp[i], i))
    q = deque(priority)
    arr = []
    while True:
        if len(q) == 0:
            break
        pop_out = q.popleft()
        if len(q) == 0:
            arr.append(pop_out)
            break
        flag = False
        for i in range(len(q)):
            if pop_out[0] < q[i][0]:
                flag = True

        if flag:
            q.append(pop_out)
        else:
            arr.append(pop_out)

    answer = 0
    for i in range(len(arr)):
        if arr[i][1] == m:
            answer = i + 1
            break

    print(answer)



