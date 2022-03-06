t = int(input())
for _ in range(t):
    logger = input()
    stack1, stack2 = [], []

    for char in logger:
        if char == '<':
            if stack1:
                stack2.append(stack1.pop())
            else:
                continue
        elif char == '>':
            if stack2:
                stack1.append(stack2.pop())
            else:
                continue
        elif char == '-':
            if stack1:
                stack1.pop()
            else:
                continue
        else:
            stack1.append(char)

    answer = ''.join(stack1) + ''.join(reversed(stack2))
    print(answer)
