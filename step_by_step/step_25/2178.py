import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
inlst = [list(map(int, list(*input().split()))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
que = deque([[0,0]])
visited[0][0] = 1
while True:
	x, y = que.popleft()
	if x == n-1 and y == m-1:
		break
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if -1 < nx < n and -1 < ny < m and inlst[nx][ny] and not visited[nx][ny]:
			inlst[nx][ny] += inlst[x][y]
			visited[nx][ny] = 1
			que.append([nx,ny])

print(inlst[n-1][m-1])
