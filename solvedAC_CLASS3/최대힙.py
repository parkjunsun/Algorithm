import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    op = int(input())
    if op == 0:
        if len(q) == 0:
            print(0)
        else:
            x = heapq.heappop(q) * -1
            print(x)
    else:
        heapq.heappush(q, op*-1)
