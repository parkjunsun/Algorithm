tmp = input().split('-')
ex = []
for item in tmp:
    ex.append(item.lstrip('0'))
arr = []

for item in ex:
    sp = item.split('+')
    sp = list(map(int, sp))
    arr.append(sum(sp))

total = arr[0]

for i in range(1, len(arr)):
    total -= arr[i]

print(total)
