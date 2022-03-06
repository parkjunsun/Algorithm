n, m = map(int, input().split())
parent = [i for i in range(n)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

tmp = 0
ans = 0

for i in range(1, m+1):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        tmp = i
        if ans == 0:
            ans = tmp
    else:
        union_parent(a, b)

if ans == 0:
    print(0)
else:
    print(ans)

