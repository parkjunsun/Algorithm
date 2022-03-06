import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit()

fidx = 2
bidx = 7
add = 6
diff = 12
dist = 2
while True:
    if fidx <= n <= bidx:
        break
    tmp = bidx
    bidx += diff
    diff += add
    fidx = tmp + 1
    dist += 1

print(dist)


