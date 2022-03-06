n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
max_num = 0

for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            sums = cards[i] + cards[j] + cards[k]
            if sums <= m:
                max_num = max(max_num, sums)

print(max_num)


