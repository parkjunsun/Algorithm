n = int(input())
forward = []
backward = []
for _ in range(n):
    pw = input()
    forward.append(pw)
    backward.append(pw[::-1])

for word in forward:
    if word in backward:
        answer = word
        break

print(len(answer), answer[len(answer)//2])