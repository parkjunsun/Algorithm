import sys

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    info = sys.stdin.readline().rstrip().split()
    dic[info[0]] = info[1]

for _ in range(m):
    addr = input()
    print(dic[addr])