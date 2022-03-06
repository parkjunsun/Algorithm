s = input()

alpha = []
sums = 0

for c in s:
    if c.isalpha():
        alpha.append(c)
    else:
        sums += int(c)
alpha.sort()
alpha = ''.join(alpha)
answer = alpha + str(sums)
print(answer)