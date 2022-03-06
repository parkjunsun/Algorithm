from collections import deque
import sys

n = int(input())
if n == 1:
    print(1)
    sys.exit()
arr = deque([i for i in range(1, n+1)])

while True:
    arr.popleft()
    if len(arr) == 1:
        break
    arr.append(arr.popleft())

print(arr[0])