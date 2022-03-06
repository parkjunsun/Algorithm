import sys

input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))

p = [0] * (n+1)
for i in range(n):
    add = p[i] + arr[i]
    p[i+1] = add

for _ in range(t):
    a, b = map(int, input().split())
    print(p[b] - p[a-1])
