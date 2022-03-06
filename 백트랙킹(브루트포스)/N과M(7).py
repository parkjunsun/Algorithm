n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def recursive(a):
    if len(a) == m:
        for num in a:
            print(num, end=' ')
        print()
        return

    for item in arr:
        a.append(item)
        recursive(a)
        a.pop()

recursive([])



