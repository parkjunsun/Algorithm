n = int(input())
result = []
stack = []
count = 0
flag = True
for _ in range(n):
    num = int(input())

    while True:
        if count >= num:
            break
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if not flag:
    print("NO")
else:
    for op in result:
        print(op)


