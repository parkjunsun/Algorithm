from collections import deque
import sys

n, k = map(int, input().split())

if n == 1:
    print("<1>")
    sys.exit()

q = deque()
res = []
for i in range(1, n+1):
    q.append(i)

while True:
    if len(res) == n:
        break
    for i in range(k-1):
        q.append(q.popleft())
    res.append(q.popleft())

ans = ""
for i in range(len(res)):
    if i == 0:
        ans += '<' + str(res[i]) + ', '
    elif i == len(res) - 1:
        ans += str(res[i]) + '>'
    else:
        ans += str(res[i]) + ', '

print(ans)
