n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
tmp = []


while True:
    if len(arr) == 0:
        break
    for i in range(k-1):
        arr.append(arr[0])
        arr.pop(0)
    tmp.append(arr.pop(0))

answer = "<"

for num in tmp:
    answer += str(num) + ", "

answer = list(answer)
answer[-2:] = '>'
print(''.join(answer))