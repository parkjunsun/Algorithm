k = int(input())
find = "IO" * k + 'I'
n = int(input())
task = input()
task += '@@'

index = 0
cnt = 0
while True:
    if index > len(task) - len(find):
        break
    if task[index:index+len(find)] == find:
        index += 2
        cnt += 1
    else:
        index += 1

print(cnt)
