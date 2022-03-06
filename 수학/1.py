try:
    while 1:
        n = int(input())
        num = '1'
        cnt = 1
        while True:
            if int(num) % n == 0:
                break
            num += '1'
            cnt += 1
        print(cnt)
except:
    exit()
