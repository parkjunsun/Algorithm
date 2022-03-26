import math

n, m = map(int, input().split())
val1 = math.gcd(n, m)
val2 = (n*m) // val1

print(val1)
print(val2)