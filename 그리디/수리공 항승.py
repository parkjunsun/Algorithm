n, m = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = set()

for num in arr:
    new_arr.add(num-0.5)
    new_arr.add(num)
    new_arr.add(num+0.5)

new_arr = list(new_arr)
new_arr.sort()

idx = 0
cnt = 0
for i in range(len(new_arr)):
    if new_arr[idx] + m < new_arr[i]:
        cnt += 1
        idx = i

if new_arr[idx] + m >= new_arr[-1]:
    cnt += 1
print(cnt)

