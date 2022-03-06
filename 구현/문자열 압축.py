def solution(string):
    if len(string) == 1:
        return 1
    min_len = int(1e9)
    length = len(string)
    for k in range(1, length//2 + 1):
        stack = []
        start = 0
        tmp = ""
        for j in range(0, length, k):
            stack.append(string[start:start+k])
            start += k
        cnt = 1
        for i in range(len(stack)-1):
            if stack[i] == stack[i+1]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += stack[i]
                else:
                    tmp += str(cnt) + stack[i]
                cnt = 1
            if i == len(stack)-2:
                if cnt == 1:
                    tmp += stack[i+1]
                else:
                    tmp += str(cnt) + stack[i+1]
        min_len = min(min_len, len(tmp))

    return min_len

print(solution("a"))