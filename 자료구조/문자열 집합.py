n, m = map(int, input().split())
s = set()
for _ in range(n):
    string = input()
    s.add(string)

cnt = 0
for _ in range(m):
    string = input()
    if string in s:
        cnt += 1

print(cnt)


"""
배열에서 원소 x 가 있는지 검사할 때 list안에서 찾으면 list전체를 다 찾기 때문에 O(n)시간 복잡도
배열에서 원소 x 가 있는지 검사할 때 set안에서 찾으면 hast table을 이용하기 때문에 O(1)에 판별가능
"""