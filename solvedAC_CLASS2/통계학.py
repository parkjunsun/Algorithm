from collections import Counter
import math

n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

arr.sort()
print(round(sum(arr) / n))
print(arr[n//2])
most = list(Counter(arr).most_common())
most.sort(key=lambda x:(-x[1], x[0]))

if len(most) > 1 and most[0][1] == most[1][1]:
    print(most[1][0])
else:
    print(most[0][0])

print(max(arr) - min(arr))
