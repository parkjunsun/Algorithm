n = int(input())
sums = 0
start = 1
zero = False
while True:
    if start > n:
        zero = True
        break

    str_str = str(start)
    sums = start
    for i in range(len(str_str)):
        sums += int(str_str[i])

    if sums == n:
        break
    start += 1

if zero:
    print(0)
else:
    print(start)