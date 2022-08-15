import sys

input = sys.stdin.readline
n, m = map(int, input().split())
inlst = []
for _ in range(n):
	inlst.append(list(map(int, input().split())))
lst = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
	for j in range(1, n+1):
		lst[i][j] = lst[i-1][j] + lst[i][j-1] - lst[i-1][j-1] + inlst[i-1][j-1]
for _ in range(m):
	x1, y1, x2, y2 = map(int, input().split())
	print(lst[x2][y2] - lst[x1-1][y2] - lst[x2][y1-1] + lst[x1-1][y1-1])