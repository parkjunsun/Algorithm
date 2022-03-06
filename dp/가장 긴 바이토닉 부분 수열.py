n = int(input())
forward_arr = list(map(int, input().split()))
backward_arr = forward_arr[::-1]

f_dp = [1] * n
b_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if forward_arr[i] > forward_arr[j]:
            f_dp[i] = max(f_dp[i], f_dp[j] + 1)

for i in range(1, n):
    for j in range(i):
        if backward_arr[i] > backward_arr[j]:
            b_dp[i] = max(b_dp[i], b_dp[j] + 1)

answer = -1
for i in range(n):
    answer = max(f_dp[i] + b_dp[n-1-i] - 1, answer)

print(answer)

