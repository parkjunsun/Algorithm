s = input()
stack = [int(s[0])]

answer = int(s[0])

for i in range(1, len(s)):
    if stack[-1] == 0 or stack[-1] == 1:
        answer += int(s[i])
        stack.append(s[i])
    else:
        answer *= int(s[i])
        stack.append(s[i])

print(answer)
