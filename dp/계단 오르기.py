import sys

n = int(input())
arr = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = int(input())


dp = [0] * (n+1)
dp[1] = arr[1]
if n == 1:
    print(dp[1])
    sys.exit()
dp[2] = max(arr[1] + arr[2], arr[2])
if n == 2:
    print(dp[2])
    sys.exit()
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])


# 특정 계단까지 올라왔을 때를 먼저 가정하자
# 만약 i번 까지 올라왔다면 2가지 방식으로만 올라왔을것이다.
# 1. 전전번 계단에서 올라와서 i를 밟은 경우
# 2. 전전전번 계단에서 올라오고 i-1번째를 밟고 i를 밟은 경우
for i in range(3, n+1):
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])



print(dp[n])