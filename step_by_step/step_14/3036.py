import math

n = int(input())
lst = list(map(int, input().split()))
for i in range(1, n):
	gcd = math.gcd(lst[0], lst[i])
	print(f'{lst[0]//gcd}/{lst[i]//gcd}')
