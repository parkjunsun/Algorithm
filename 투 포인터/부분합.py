n, s = map(int, input().split())
arr = list(map(int, input().split()))

sums = 0
right = 0
length = 0
mn = float('inf')

for left in range(n):
    while right < n and sums <= s:
        sums += arr[right]
        right += 1
        length += 1
    if sums >= s:
        mn = min(mn, length)
    sums -= arr[left]
    length -= 1

if mn == float('inf'):
    print(0)
else:
    print(mn)