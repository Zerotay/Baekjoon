import sys
input = sys.stdin.readline

n = int(input())
inlst = [*map(int, input().split())]
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
	dp[i][i] = 1
for i in range(1, n):
	dp[i-1][i] = 1 if inlst[i-1] == inlst[i] else 0
for i in range(2, n):
	for j in range(n-i):
		dp[j][j+i] = 1 if dp[j+1][j+i-1] and inlst[j] == inlst[j+i] else 0

for _ in range(m):
	s, e = map(int, input().split())
	print(dp[s-1][e-1])