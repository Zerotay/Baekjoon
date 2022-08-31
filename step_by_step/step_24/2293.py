import sys
input = sys.stdin.readline

n, k = map(int, input().split())
inlst = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in inlst:
	for j in range(i, k+1):
			dp[j] += dp[j-i]
print(dp[k])