n, k = map(int, input().split())
lst = list(map(int, input().split()))
dp = [0, lst[0]]
for i in range(1, n):
	dp.append(dp[i] + lst[i])
mx = -10000001
for i in range(n - k + 1):
	mx = max(mx, dp[i+k] - dp[i])
print(mx)