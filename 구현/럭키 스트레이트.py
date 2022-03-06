n = int(input())
n = str(n)

left = n[:len(n)//2]
right = n[len(n)//2:]

l_score, r_score = 0, 0

for i in range(len(left)):
    l_score += int(left[i])
for i in range(len(right)):
    r_score += int(right[i])

if l_score == r_score:
    print("LUCKY")
else:
    print("READY")
