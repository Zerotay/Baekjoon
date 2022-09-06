import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
	inlst[x][y] = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if -1 < nx < m and -1 < ny < n and inlst[nx][ny]:
			dfs(nx,ny)

for _ in range(int(input())):
	m, n, k = map(int, input().split())
	inlst = [[0] * n for _ in range(m)]
	answer = 0
	for _ in range(k):
		x, y = map(int, input().split())
		inlst[x][y] = 1
	for i in range(m):
		for j in range(n):
			if inlst[i][j]:
				answer += 1
				dfs(i, j)
	print(answer)