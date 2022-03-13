from bisect import bisect_left
from bisect import bisect_right

n = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

m = int(input())
t = list(map(int, input().split()))

for num in t:
    left = bisect_left(arr, num)
    right = bisect_right(arr, num)
    print(right - left)