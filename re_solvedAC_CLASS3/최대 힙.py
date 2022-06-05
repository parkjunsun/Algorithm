import heapq
import sys

input = sys.stdin.readline
q = []

n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(q) <= 0:
            print(0)
        else:
            print(heapq.heappop(q) * -1)
    else:
        heapq.heappush(q, num * -1)
