import heapq

n = int(input())
q = []
for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)


total = 0
while True:
    n1 = heapq.heappop(q)
    if len(q) == 0:
        break
    n2 = heapq.heappop(q)
    hap = n1 + n2
    total += hap
    heapq.heappush(q, hap)

print(total)
