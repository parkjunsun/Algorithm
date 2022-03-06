n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()

answer = dist[0] * price[0]
pivot = price[0]

pidx = []

for i in range(1, len(dist)):
    if pivot <= price[i]:
        pidx.append((pivot, dist[i]))
    else:
        pivot = price[i]
        pidx.append((pivot, dist[i]))

for item in pidx:
    answer += item[0] * item[1]

print(answer)
