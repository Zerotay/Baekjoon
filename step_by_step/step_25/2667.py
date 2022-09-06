import sys
input = sys.stdin.readline

n = int(input())
inlst = [[*map(int, *input().split())] for _ in range(n)]
answer = []
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
	global count
	count += 1
	inlst[x][y] = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if -1 < nx < n and -1 < ny < n and inlst[nx][ny]:
			dfs(nx, ny)

for i in range(n):
	for j in range(n):
		if inlst[i][j]:
			count = 0
			dfs(i,j)
			answer.append(count)

print(len(answer))
print(*sorted(answer), sep='\n')