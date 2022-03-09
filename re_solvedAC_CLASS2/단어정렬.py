n = int(input())
arr = []
for _ in range(n):
    word = input()
    length = len(word)
    arr.append((word, length))

arr = list(set(arr))
arr.sort(key=lambda x:(x[1], x[0]))

for w in arr:
    print(w[0])
