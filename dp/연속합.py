n = int(input())
dp = [0] * n
arr = list(map(int, input().split()))
dp[0] = arr[0]
sums = dp[0]
flag = False
for i in range(1, n):
    sums += arr[i]
    if sums < 0:
        sums = 0
    dp[i] = max(dp[i], sums)

for num in arr:
    if num >= 0:
        flag = True

if flag:
    print(max(dp))
else:
    arr.sort(reverse=True)
    print(arr[0])