n = int(input())

for i in range(1, n + 1):
    main = i
    sub = 0
    for char in str(i):
        sub += int(char)

    if main + sub == n:
        break

if main == n:
    print(0)
else:
    print(main)

