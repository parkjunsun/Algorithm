n = int(input())
arr = list(map(int, input().split()))
arr.sort()
idx = len(arr) // 2 - 1

print(arr[idx])

