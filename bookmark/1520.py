import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

m, n = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(m)]

lst = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]

def dfs(x, y):
	if x == m-1 and y == n-1: return 1
	if lst[x][y] == -1:
		lst[x][y] = 0
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if -1<nx<m and -1<ny<n and inlst[x][y] > inlst[nx][ny]:
				lst[x][y] += dfs(nx, ny)
	return lst[x][y]

print(dfs(0,0))
