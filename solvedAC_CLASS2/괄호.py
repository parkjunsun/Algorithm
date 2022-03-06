n = int(input())
for _ in range(n):
    ps = input()
    stack = []
    flag = False
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if len(stack) == 0:
                print("NO")
                flag = True
                break
            else:
                stack.pop()
    if not flag:
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")