n = int(input())
val = input()

ans = 0

for i in range(n):
    ans += (ord(val[i]) - 96) * (31 ** i)
print(ans % 1234567891)
