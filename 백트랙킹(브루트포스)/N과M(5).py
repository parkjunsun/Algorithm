n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = []

def recursive(a):
    if len(a) == m:
        for num in a:
            print(num, end=' ')
        print()
        return

    for item in arr:
        if item not in visited:
            visited.append(item)
            a.append(item)
            recursive(a)
            visited.pop()
            a.pop()

recursive([])