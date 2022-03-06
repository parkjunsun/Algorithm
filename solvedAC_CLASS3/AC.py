from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input()
    p = p.replace("RR", "")
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip().rstrip(']').lstrip('[').split(','))
    flag = False

    for op in p:
        if op == 'R':
            arr.reverse()
        elif op == 'D':
            if (len(arr) == 1 and arr[0] == '') or len(arr) == 0:
                flag = True
                break
            else:
                arr.popleft()

    answer = '['
    if flag:
        print("error")
    else:
        for i in range(len(arr)):
            if i == len(arr)-1:
                answer += arr[i]
            else:
                answer += arr[i] + ','
        answer += ']'
        print(answer)
