from collections import Counter

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
counter = Counter(arr).most_common()
counter.sort(key=lambda x:(-x[1], x[0]))

avg = round(sum(arr) / len(arr))
mid = arr[len(arr)//2]
if len(arr) > 1:
    if counter[0][1] == counter[1][1]:
        most = counter[1][0]
    else:
        most = counter[0][0]
else:
    most = counter[0][0]

rng = max(arr) - min(arr)

print(avg)
print(mid)
print(most)
print(rng)


