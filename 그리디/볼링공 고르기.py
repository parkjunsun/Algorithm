n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = []

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] != arr[j]:
            ans.append((arr[i], arr[j]))

print(len(ans))