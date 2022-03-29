while True:
    stack = []
    flag = False
    line = input()
    if line == '.':
        break
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                flag = True
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = True
        elif char == ']':
            if len(stack) == 0:
                flag = True
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                flag = True

    if len(stack) != 0:
        flag = True

    if flag:
        print("no")
    else:
        print("yes")


