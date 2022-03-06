import math

arr = [1 for _ in range(1000001)]
arr[0] = 0
arr[1] = 0

for i in range(2, int(math.sqrt(1000001)) + 1):
    if arr[i] == 1:
        gop = 2
        while i*gop <= 1000000:
            arr[i*gop] = 0
            gop += 1

for i in range(2, len(arr)):
    if i % 2 == 0:
        arr[i] = 0

while True:
    flag = False
    n = int(input())
    if n == 0:
        break
    for i in range(3, n+1):
        if arr[i] == 1 and arr[n-i] == 1:
            print(f"{n} = {i} + {n-i}")
            flag = True
            break

    if not flag:
        print("Goldbach's conjecture is wrong.")

