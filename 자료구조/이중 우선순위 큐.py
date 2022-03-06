import heapq

left = []
heapq.heapify(left)

right = []
heapq.heapify(right)

n = int(input())
for _ in range(n):
    cmds = input().split()
    cmd = cmds[0]
    val = int(cmds[1])
    if cmd == 'I':
        heapq.heappush(left, val)
        heapq.heappush(right, -val)
    elif cmd == 'D':
        if len(left) == 0 and len(right) == 0:
            continue
        if val == -1:
            heapq.heappop(left)
        else:
            heapq.heappop(right)

print(left)
print(right)
print()
print(-right[0])
print(left[0])


