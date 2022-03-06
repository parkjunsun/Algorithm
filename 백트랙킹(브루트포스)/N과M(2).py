n, m = map(int, input().split())
visited = [0] * (n+1)

def recursive(arr, start):
    if len(arr) == m:
        for num in arr:
            print(num, end=' ')
        print()
        return

    for i in range(start, n+1):
        if visited[i] == 0:
            arr.append(i)
            visited[i] = 1
            recursive(arr, i+1)
            visited[i] = 0
            arr.pop()

recursive([], 1)