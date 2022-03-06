import heapq

n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append((s, t))

arr.sort(key=lambda x:x[0])

q = []
heapq.heappush(q, arr[0][1])

start = 0
cnt = 0
for i in range(1, n):
    if q[0] > arr[i][0]:
        heapq.heappush(q, arr[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, arr[i][1])

print(len(q))