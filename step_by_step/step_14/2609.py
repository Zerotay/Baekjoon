import math
n, m = map(int , input().split())
k = math.gcd(n, m)
print(k)
print(n*m//k)