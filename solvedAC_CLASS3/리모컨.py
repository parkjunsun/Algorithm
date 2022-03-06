n = int(input())
m = int(input())

if m != 0:
    arr = list(map(str, input().split()))
else:
    arr = []

min_num = abs(n-100)

for i in range(1000001):
    flag = False
    num_arr = list(str(i))

    for num in num_arr:
        if num in arr:
            flag = True
            break

    if flag:
        continue
    else:
        min_num = min(min_num, abs(n-i) + len(str(i)))

print(min_num)
