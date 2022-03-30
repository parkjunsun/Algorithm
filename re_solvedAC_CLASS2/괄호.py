n = int(input())

for _ in range(n):
    stack = []
    flag = False
    vps = input()
    for char in vps:
        if char == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                flag = True
                break

            if stack[-1] == '(':
                stack.pop()

    if len(stack) != 0:
        flag = True

    if flag:
        print("NO")
    else:
        print("YES")
