import sys
import math

input = sys.stdin.readline
n = int(input())
lst = list(int(input()) for _ in range(n))
lst.sort()
gcd = lst[1] - lst[0]
for i in range(2, len(lst)):
	gcd = math.gcd(gcd, lst[i] - lst[i - 1])
answer = [gcd]
for i in range(2, int(gcd ** 0.5) + 1):
	if gcd % i == 0:
		answer.append(i)
		answer.append(gcd // i)
if (gcd ** 0.5).is_integer():
	answer.pop()
print(*sorted(answer))
