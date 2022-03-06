t = int(input())

for _ in range(t):
    n, m, num = map(int, input().split())

    hotel = [[""] * m for _ in range(n)]
    count = 0
    flag = False

    for i in range(m):
        for j in range(n-1, -1, -1):
            count += 1
            if len(str(i+1)) == 1:
                room_num = '0' + str(i+1)
            else:
                room_num = str(i+1)
            hotel[j][i] = str(n - j) + room_num
            if count == num:
                answer = hotel[j][i]
                flag = True
                break
        if flag:
            break

    print(answer)


