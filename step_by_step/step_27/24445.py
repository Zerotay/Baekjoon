import sys
from collections import deque
input = sys.stdin.readline

n, m , r = map(int, input().split())
paths = [[] for _ in range(n+1)]
for _ in range(m):
	s, e = map(int, input().split())
	paths[s].append(e)
	paths[e].append(s)
paths = [*map(lambda x: sorted(x, reverse=True), paths)]
visited = [0 for _ in range(n+1)]
que = deque([r])
count = 1
visited[r] = count
while que:
	top = que.popleft()
	for i in paths[top]:
		if not visited[i]:
			count += 1
			visited[i] = count
			que.append(i)
print(*visited[1:], sep='\n')
