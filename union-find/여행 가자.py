n = int(input())
m = int(input())

parent = [i for i in range(n+1)]


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


for i in range(n):
    rel = list(map(int, input().split()))
    for j in range(len(rel)):
        if rel[j] == 1:
            union_parent(i+1, j+1)

path = list(map(int, input().split()))
ans = []
for item in path:
    ans.append(find_parent(item))

pivot = ans[0]

if ans.count(pivot) == len(path):
    print("YES")
else:
    print("NO")