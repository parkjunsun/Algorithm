n = int(input())
result = []
stack = []
cnt = 0

for _ in range(n):
    num = int(input())

    while True:
        if cnt >= num:
            break
        cnt += 1
        result.append('+')
        stack.append(cnt)

    if stack[-1] == num:
        result.append('-')
        stack.pop()

if len(stack) != 0:
    print("NO")
else:
    for op in result:
        print(op)
