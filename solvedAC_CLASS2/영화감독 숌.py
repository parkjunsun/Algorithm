n = int(input())

index = 666
cnt = 0
answer = ""

while True:
    if cnt == n:
        break
    str_index = str(index)
    if str_index.find("666") != -1:
        cnt += 1
    index += 1
    answer = str_index

print(answer)


