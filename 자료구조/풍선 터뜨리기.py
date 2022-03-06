from collections import deque

n = int(input())
a = list(map(int, input().split()))
q = deque()
for i in range(1, len(a)+1):
    q.append((a[i-1], i))

answer = []
out = q.popleft()
answer.append(out[1])

while True:
    if len(q) == 0:
        break
    if out[0] > 0:
        rot_idx = -out[0] + 1
    else:
        rot_idx = -out[0]
    q.rotate(rot_idx)
    out = q.popleft()
    answer.append(out[1])

for num in answer:
    print(num, end=' ')
