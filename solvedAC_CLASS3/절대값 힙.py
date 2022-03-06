import heapq
import sys

input = sys.stdin.readline

q = []

n = int(input())
for _ in range(n):
    val = int(input())
    if val != 0:
        heapq.heappush(q, (abs(val), val))
    else:
        if len(q) == 0:
            print(0)
        else:
            var, ori = heapq.heappop(q)
            print(ori)



