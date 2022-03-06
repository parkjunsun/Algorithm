s = input()
explode = input()
length = len(explode) - 1
end = explode[-1]
stack = []

for i in range(len(s)):
    flag = False
    cnt = 0
    if s[i] != end:
        stack.append(s[i])
    else:
        if length > len(stack):
            stack.append(s[i])
            continue
        for k in range(length):
            if stack[-1 - k] != explode[-2 - k]:
                flag = True
            else:
                cnt += 1
        if not flag:
            for _ in range(cnt):
                stack.pop()
            cnt = 0
        if flag:
            stack.append(s[i])


answer = ''.join(stack)
if answer:
    print(answer)
else:
    print("FRULA")