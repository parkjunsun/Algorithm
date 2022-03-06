n = int(input())
arr = list(map(int, input().split()))
arr.sort()

possible = [arr[i] for i in range(len(arr))]
possible = list(set(possible))
sums = 0
idx = 0
cnt = 0
while True:
    sums += arr[idx]
    if sums not in possible:
        possible.append(sums)
    idx += 1
    if idx == len(arr):
        sums = 0
        cnt += 1
        idx = cnt
    if cnt == len(arr) - 1:
        break
possible.sort()
i = 1
while True:
    if i not in possible:
        print(i)
        break
    i += 1