n, k = map(int, input().split())
p = 1000000007

def factor(n):
	result = 1
	for i in range(2, n+1):
		result = (result * i) % p
	return result

def sqr(n, k):
	if k == 0:
		return 1
	elif k == 1:
		return n

	tmp = sqr(n, k//2)
	if k % 2:
		return tmp * tmp * n % p
	else:
		return tmp * tmp % p

print(factor(n) * sqr(factor(n-k) * factor(k), p-2) % p)