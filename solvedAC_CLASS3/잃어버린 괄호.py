expression = input().split('-')
result = 0
parse = []
for i in range(len(expression)):
    sp = list(map(int, expression[i].split('+')))
    parse.append(sp)

for i in range(len(parse)):
    if i == 0:
        result = sum(parse[i])
    else:
        result -= sum(parse[i])

print(result)