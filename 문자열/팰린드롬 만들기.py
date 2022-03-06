name = input()
alpha = [0] * 26

for char in name:
    alpha[ord(char)-65] += 1

odd = 0
front = ""
for i in range(len(alpha)):
    if alpha[i] % 2 == 1:
        odd += 1
        tmp = chr(i+65)
    front += chr(i+65) * (alpha[i] // 2)

back = front[::-1]

if odd > 1:
    print("I'm Sorry Hansoo")
elif odd == 1:
    print(front + tmp + back)
else:
    print(front + back)