import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m, n = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(n)]
que = deque()
for i in range(n):
	for j in range(m):
		if inlst[i][j] == 1:
			que.append([i,j])
while que:
	tx, ty = que.popleft()
	for i in range(4):
		nx, ny = tx + dx[i], ty + dy[i]
		if -1<nx<n and -1<ny<m and not inlst[nx][ny]:
			inlst[nx][ny] = inlst[tx][ty] + 1
			que.append([nx, ny])
mx = 0
for i in inlst:
	if 0 in i:
		print(-1)
		exit(0)
	mx = max(mx, *i)
print(mx-1)