import sys

input = sys.stdin.readline
n = int(input())
ab = []
for _ in range(n):
	ab.append(list(map(int, input().split())))
ab.sort()
lst = [ab[i][1] for i in range(n)]
dp = [0] * n
for i in range(n):
	for j in range(i):
		if lst[i] > lst[j] and dp[i] < dp[j]:
			dp[i] = dp[j]
	dp[i] += 1
print(n - max(dp))