import sys

n = int(input())
arr = [0] * 10001

max_num = -int(1e9)
min_num = int(1e9)

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    max_num = max(max_num, num)
    min_num = min(min_num, num)
    arr[num] += 1

for i in range(min_num, max_num + 1):
    for j in range(arr[i]):
        print(i)
