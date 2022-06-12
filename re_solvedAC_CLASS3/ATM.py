n = int(input())
arr = list(map(int, input().split()))

arr.sort()
total = 0

for i in range(len(arr)):
    sums = 0
    for j in range(i+1):
        sums += arr[j]
    total += sums

print(total)
