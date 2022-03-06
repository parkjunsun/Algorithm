import sys

n = int(input())
arr = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(input())

if n == 1:
    print(arr[1])
    sys.exit()
elif n == 2:
    print(arr[1]+arr[2])
    sys.exit()

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

dp[3] = max(arr[1]+arr[3], arr[2]+arr[3], dp[2])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

print(max(dp))

# 계단 오르기 문제는 i번째 계단을 꼭 밟아야 한다는 조건이 있음
# 그러나 포도주 시식 문제는 i번째 포도주를 꼭 먹어야한다는 조건이 없음
# 즉, i번째 포도주를 먹지 않았을 경우에 최대가 생기는 테스트케이스가 존재
# [1000, 1000, 1, 1, 1000, 1000]과 같은 경우 1을 먹지 않아야 최대가 됨