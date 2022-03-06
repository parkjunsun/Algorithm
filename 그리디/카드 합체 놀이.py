import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

for _ in range(m):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    hap = a + b
    heapq.heappush(arr, hap)
    heapq.heappush(arr, hap)

print(sum(arr))

