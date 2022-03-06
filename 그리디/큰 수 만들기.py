n = int(input())
arr = list(map(str, input().split()))

save = []
for i in range(len(arr)):
    save.append((arr[i]*9, arr[i]))

save.sort(key=lambda x:x[0], reverse=True)

answer = ""
for item in save:
    answer += item[1]

flag = False
for num in answer:
    if num != '0':
        flag = True

if not flag:
    print(0)
else:
    print(answer)