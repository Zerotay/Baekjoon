import sys
input = sys.stdin.readline
from collections import deque

dx =[2, 2, 1, 1, -1, -1, -2, -2]
dy =[1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(int(input())):
	i = int(input())
	scx, scy = map(int, input().split())
	dtx, dty = map(int, input().split())
	lst = [[0] * i for _ in range(i)]
	que = deque([[scx, scy]])
	while que:
		top = que.popleft()
		if top == [dtx, dty]:
			break
		for j in range(8):
			nx = top[0] + dx[j]
			ny = top[1] + dy[j]
			if -1 < nx < i and -1 < ny < i and not lst[nx][ny]:
				lst[nx][ny] = lst[top[0]][top[1]] + 1
				que.append([nx, ny])
	print(lst[dtx][dty])
