import sys
input = sys.stdin.readline

for _ in range(int(input())):
	k = int(input())
	inlst = [0] + [*map(int, input().split())]
	answer = 0
	sumlst = [0 for _ in range(k+1)]
	for i in range(1, k+1):
		sumlst[i] = sumlst[i-1] + inlst[i]

	dp = [[0 for _ in range(k+1)] for _ in range(k+1)]
	for i in range(2, k+1):
		for j in range(1, k+2-i):
			dp[j][j+i-1] = min([dp[j][j+l] + dp[j+l+1][j+i-1] for l in range(i-1)]) \
				+ sumlst[j+i-1] - sumlst[j-1]
	print(dp[1][k])
