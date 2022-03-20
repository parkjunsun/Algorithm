import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit()

start = 2
end = 7
rng = 12
cnt = 2
add = 6

while True:
    if start <= n <= end:
        break
    start += add
    end += rng
    add += 6
    rng += 6
    cnt += 1

print(cnt)
