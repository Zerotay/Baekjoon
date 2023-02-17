import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

m, n, h = map(int, input().split())
inlst = [[[*map(int, input().split())] for _ in range(n)] for _ in range(h)]
que = deque()
for i in range(h):
	for j in range(n):
		for k in range(m):
			if inlst[i][j][k] == 1:
				que.append([i,j,k])
while que:
	tx, ty, tz = que.popleft()
	for i in range(6):
		nx, ny, nz = tx + dx[i], ty + dy[i], tz + dz[i]
		if -1 < nx < h and -1 < ny < n and -1 < nz < m and not inlst[nx][ny][nz]:
			inlst[nx][ny][nz] = inlst[tx][ty][tz] + 1
			que.append([nx, ny, nz])
mx = 0
for i in range(h):
	for j in range(n):
		if 0 in inlst[i][j]:
			print(-1)
			exit(0)
		mx = max(mx, *inlst[i][j])
print(mx-1)