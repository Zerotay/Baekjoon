def fact(n, m):
	ans = 0
	i = m
	while i <= n:
		ans += n // i
		i *= m
	return ans

n, m = map(int, input().split())
num5 = fact(n, 5) - fact(n - m, 5) - fact(m, 5)
num2 = fact(n, 2) - fact(n - m, 2) - fact(m, 2)
print(min(num5, num2))