n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def recursive(a, start):
    if len(a) == m:
        for num in a:
            print(num, end=' ')
        print()
        return

    for item in arr:
        if item >= start:
            a.append(item)
            recursive(a, item)
            a.pop()

recursive([], arr[0])