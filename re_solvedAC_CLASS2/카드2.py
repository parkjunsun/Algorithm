from collections import deque

n = int(input())
q = deque()
for i in range(1, n + 1):
    q.append(i)

while True:
    if len(q) == 1:
        break
    q.popleft()
    q.append(q.popleft())

print(q[0])
