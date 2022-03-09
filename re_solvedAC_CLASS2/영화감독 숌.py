n = int(input())
cnt = 0
start = 666

while True:
    if cnt == n:
        break
    if str(start).find("666") != -1:
        cnt += 1
    start += 1

print(start-1)