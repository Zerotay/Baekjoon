import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
n, m = map(int, input().split())
inlst = [[*map(int,*list(input().split()))] for _ in range(n)]
lst = [[[0] * 2 for _ in range(m)] for _ in range(n)]
que = deque([[0,0,0]])
while que:
	tx, ty, tz = que.popleft()
	if tx == n-1 and ty == m-1:
		print(lst[tx][ty][tz] + 1)
		exit(0)
	for i in range(4):
		nx, ny = tx + dx[i], ty + dy[i]
		if -1 < nx < n and -1 < ny < m:
			if inlst[nx][ny] == 1 and not tz:
				lst[nx][ny][1] = lst[tx][ty][0] + 1
				que.append([nx,ny,1])
			elif not inlst[nx][ny] and not lst[nx][ny][tz]:
				lst[nx][ny][tz] = lst[tx][ty][tz] + 1
				que.append([nx,ny,tz])
print(-1)