n = int(input())
total = list(map(int, input().split()))
cards = {}

for num in total:
    if num not in cards:
        cards[num] = 1
    else:
        cards[num] += 1

m = int(input())
arr = list(map(int, input().split()))

for item in arr:
    if item not in cards:
        print(0, end=' ')
    else:
        print(cards[item], end=' ')