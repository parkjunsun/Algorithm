n = int(input())
arr = list(map(int, input().split()))
arr.sort()


left, right = 0, len(arr) - 1
min_num = float('inf')

ans1, ans2 = 0, 0

while left < right:
    sums = arr[left] + arr[right]
    if abs(sums) < min_num:
        min_num = abs(sums)
        ans1 = left
        ans2 = right
    if sums < 0:
        left += 1
    else:
        right -= 1

print(arr[ans1], arr[ans2])
