n = int(input())

lst = [0] * (n + 1)
lst[0] = 1
lst[1] = 1
def dp(n):
	if lst[n] != 0:
		return lst[n]
	lst[n] = dp(n-1) + dp(n-2)
	return lst[n]

print(dp(n - 1), n - 2)