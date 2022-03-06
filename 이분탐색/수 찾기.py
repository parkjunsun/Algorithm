n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
arr = list(map(int, input().split()))

start = 0
end = len(a) - 1


def binary_search(a, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return 1
        elif a[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for num in arr:
    find = binary_search(a, num, start, end)
    print(find)
