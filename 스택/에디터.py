string = input()
n = int(input())
stack1, stack2 = [i for i in string], []

for _ in range(n):
    cmd = input()
    if len(cmd) == 1:
        if cmd == 'L':
            if stack1:
                stack2.append(stack1.pop())
            else:
                continue
        elif cmd == 'D':
            if stack2:
                stack1.append(stack2.pop())
            else:
                continue
        elif cmd == 'B':
            if stack1:
                stack1.pop()
            else:
                continue
    else:
        command, char = cmd[0], cmd[2]
        if command == 'P':
            stack1.append(char)

answer = ''.join(stack1) + ''.join(reversed(stack2))
print(answer)