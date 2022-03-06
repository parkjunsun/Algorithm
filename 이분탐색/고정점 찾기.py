n = int(input())
arr = list(map(int, input().split()))

start = 0
end = len(arr) - 1

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] > mid:
            start = mid + 1
        elif arr[mid] < mid:
            end = mid - 1
        else:
            return mid
    return -1

print(binary_search(start,end))



