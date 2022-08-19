def dc(n):
	if n == 1:
		return a % c
	tmp = dc(n // 2)
	if n % 2:
		return tmp * tmp * a % c
	else:
		return tmp * tmp % c

a, b, c = map(int, input().split())
print(dc(b))