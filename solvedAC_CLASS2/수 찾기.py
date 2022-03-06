n = int(input())
arr = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

arr = set(arr)

for item in num:
    if item in arr:
        print(1)
    else:
        print(0)