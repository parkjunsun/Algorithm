n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
group = 0
for n in arr:
    cnt += 1
    if cnt >= n:
        group += 1
        cnt = 0
print(group)