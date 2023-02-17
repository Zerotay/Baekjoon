n = int(input())
lst = [0 for _ in range(n+2)]

lst[1] = 1
lst[2] = 2
def dp(n):
	for i in range(3, n+1):
		lst[i] = (lst[i - 1] + lst[i - 2]) % 15746
	return lst[n]
print(dp(n))