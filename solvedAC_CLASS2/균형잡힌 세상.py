while True:
    s = input()
    stack = []
    flag = False
    if s == '.':
        break

    for char in s:
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
                break
        elif char == ']':
            if len(stack) == 0:
                flag = True
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
    if len(stack) != 0:
        flag = True

    if not flag:
        print("yes")
    else:
        print("no")