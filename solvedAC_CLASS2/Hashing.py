n = int(input())
s = input()
answer = 0
upper = 0

for char in s:
    answer += (ord(char) - 96) * 31 ** upper
    upper += 1

print(answer)