import sys
input = sys.stdin.readline

n, m = map(int, input().split())
firlst = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
seclst = [list(map(int, input().split())) for _ in range(m)]
lst = [[0] * k for _ in range(n)]
for i in range(n):
	for j in range(k):
		for p in range(m):
			lst[i][j] += firlst[i][p] * seclst[p][j]
for i in range(n):
	print(*lst[i])