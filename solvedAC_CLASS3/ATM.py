n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sums = arr[0]
add = arr[0]

for i in range(1, n):
    add += arr[i]
    sums += add

print(sums)