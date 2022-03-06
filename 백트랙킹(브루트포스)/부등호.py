num = int(input())
arr = list(map(str, input().split()))
visited = [0] * 10

def check(i,j,k):
    if k == ">":
        return i>j
    else:
        return i<j

mx, mn = "", ""

def bfs(cnt, string):
    global mx, mn
    if cnt > num:
        if len(mn) == 0:
            mn = string
        else:
            mx = string
        return
    for i in range(10):
        if visited[i] == 0:
            if cnt == 0 or check(string[-1], str(i), arr[cnt-1]):
                visited[i] = 1
                bfs(cnt+1, string + str(i))
                visited[i] = 0

bfs(0, "")
print(mx)
print(mn)