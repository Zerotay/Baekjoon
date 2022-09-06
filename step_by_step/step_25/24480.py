import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(r):
	global count
	visited[r] = count
	for i in paths[r]:
		if not visited[i]:
			count += 1
			dfs(i)

n, m, r = map(int, input().split())
paths = [[] for _ in range(n+1)]
for _ in range(m):
	s, e = map(int, input().split())
	paths[s].append(e)
	paths[e].append(s)
paths = [*map(lambda x: sorted(x, reverse=True), paths)]
visited = [0 for _ in range(n+1)]
count = 1
dfs(r)
for i in range(1, n+1):
	print(visited[i])
