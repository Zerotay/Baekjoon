import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def recur(i, j):
	if i == m-1 and j == n-1:
		return 1
	if dp[i][j] == -1:
		dp[i][j] = 0
		for k in range(4):
			tx = i + dx[k]
			ty = j + dy[k]
			if -1 < tx < m and -1 < ty < n:
				if inlst[i][j] > inlst[tx][ty]:
					dp[i][j] += recur(tx,ty)
	return dp[i][j]

m, n = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
print(recur(0, 0))