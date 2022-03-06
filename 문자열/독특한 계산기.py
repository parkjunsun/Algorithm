from collections import deque
import sys

ops = ['+', '-', '*', '/']
flag_cnt = 0

expression = input()
q = deque()
tmp = ""
for char in expression:
    if not char.isdigit():
        q.append(tmp)
        q.append(char)
        tmp = ""
    else:
        tmp += char
q.append(tmp)
if q[0] == '':
    q.popleft()

for op in ops:
    if op not in q:
        flag_cnt += 1

if flag_cnt == 4:
    print(int(''.join(q)))
    sys.exit()

if q[0] == '-' and len(q) == 2:
    print(int(''.join(q)))
    sys.exit()


if len(q) > 3:
    while True:
        if len(q) == 3:
            break
        if q[0] == '-' and len(q) == 4:
            break
        flag = 0
        if q[0] == '-':
            flag = 1
            q.popleft()

        if q[1] == '+' or q[1] == '-':
            fpri = 1
        elif q[1] == '*' or q[1] == '/':
            fpri = 2

        if q[-2] == '+' or q[-2] == '-':
            bpri = 1
        elif q[-2] == '*' or q[-2] == '/':
            bpri = 2

        if flag == 1:
            f = int(q[0]) * -1
        else:
            f = int(q[0])
        b = int(q[2])
        if fpri > bpri:
            if q[1] == '+':
                forward = f + b
            elif q[1] == '-':
                forward = f - b
            elif q[1] == '*':
                forward = f * b
            elif q[1] == '/':
                if f < 0 and b < 0:
                    forward = f // b
                elif f < 0 or b < 0:
                    forward = (abs(f) // abs(b)) * -1
                else:
                    forward = f // b

            for _ in range(3):
                q.popleft()
            q.appendleft(forward)

        elif fpri < bpri:
            if q[-2] == '+':
                backward = int(q[-3]) + int(q[-1])
            elif q[-2] == '-':
                backward = int(q[-3]) - int(q[-1])
            elif q[-2] == '*':
                backward = int(q[-3]) * int(q[-1])
            elif q[-2] == '/':
                if int(q[-3]) < 0 and int(q[-1]) < 0:
                    backward = int(q[-3]) // int(q[-1])
                elif int(q[-3]) < 0 or int(q[-1]) < 0:
                    backward = (abs(int(q[-3])) // abs(int(q[-1]))) * -1
                else:
                    backward = int(q[-3]) // int(q[-1])

            for _ in range(3):
                q.pop()
            q.append(backward)
        else:
            if q[1] == '+':
                forward = f + b
            elif q[1] == '-':
                forward = f - b
            elif q[1] == '*':
                forward = f * b
            elif q[1] == '/':
                if f < 0 and b < 0:
                    forward = f // b
                elif f < 0 or b < 0:
                    forward = (abs(f) // abs(b)) * -1
                else:
                    forward = f // b

            if q[-2] == '+':
                backward = int(q[-3]) + int(q[-1])
            elif q[-2] == '-':
                backward = int(q[-3]) - int(q[-1])
            elif q[-2] == '*':
                backward = int(q[-3]) * int(q[-1])
            elif q[-2] == '/':
                if int(q[-3]) < 0 and int(q[-1]) < 0:
                    backward = int(q[-3]) // int(q[-1])
                elif int(q[-3]) < 0 or int(q[-1]) < 0:
                    backward = (abs(int(q[-3])) // abs(int(q[-1]))) * -1
                else:
                    backward = int(q[-3]) // int(q[-1])

            if forward > backward:
                for _ in range(3):
                    q.popleft()
                q.appendleft(forward)
            elif forward < backward:
                for _ in range(3):
                    q.pop()
                q.append(backward)
            else:
                for _ in range(3):
                    q.popleft()
                q.appendleft(forward)

        if flag == 1:
            if str(q[0]).isdigit():
                q.appendleft('-')


if q[0] == '-':
    flag = 1
    q.popleft()
else:
    flag = 0

if flag == 1:
    f = int(q[0]) * -1
else:
    f = int(q[0])
b = int(q[2])

if q[1] == '+':
    print(f + b)
elif q[1] == '-':
    print(f - b)
elif q[1] == '*':
    print(f * b)
elif q[1] == '/':
    if f < 0 and b < 0:
        print(f // b)
    elif f < 0 or b < 0:
        print((abs(f) // abs(b)) * -1)
    else:
        print(f // b)