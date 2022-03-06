n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = []

def recursive(a, start):
    if len(a) == m:
        for num in a:
            print(num, end=' ')
        print()
        return

    for item in arr:
        if item >= start:
            if item not in visited:
                visited.append(item)
                a.append(item)
                recursive(a, item)
                visited.pop()
                a.pop()

recursive([], arr[0])
