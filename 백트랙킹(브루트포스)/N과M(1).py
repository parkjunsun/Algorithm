n, m = map(int, input().split())
visited = [0] * (n+1)

def recursive(arr):
    if len(arr) == m:
        for num in arr:
            print(num, end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            arr.append(i)
            visited[i] = 1
            recursive(arr)
            visited[i] = 0
            arr.pop()

recursive([])