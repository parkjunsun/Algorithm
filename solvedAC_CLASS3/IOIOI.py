n = int(input())
s = int(input())
m = input()

p = "IO" * n + 'I'
cnt = 0

for i in range(len(m) - len(p)):
    sub = ""
    for j in range(len(p)):
        sub += m[i+j]
    if sub == p:
        cnt += 1

print(cnt)
