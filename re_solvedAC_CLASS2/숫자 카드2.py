from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
chk = list(map(int, input().split()))


def count(num):
    left = bisect_left(arr, num)
    right = bisect_right(arr, num)
    return right - left


for num in chk:
    print(count(num), end=' ')
