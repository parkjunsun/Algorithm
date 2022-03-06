v, e = map(int, input().split())
parents = [i for i in range(v+1)]

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for _ in range(e):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, v+1):
    print(find_parent(i), end=' ')

print(parents)
