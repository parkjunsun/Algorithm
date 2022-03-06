s = input()

index = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        index.append(i+1)

print((len(index)+1) // 2)
