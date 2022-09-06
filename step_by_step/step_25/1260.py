import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1001)

n, m, v = map(int, input().split())
paths = {i:set() for i in range(n+1)}
for _ in range(m):
	s, e = map(int, input().split())
	paths[s].add(e)
	paths[e].add(s)
dvisited = [0 for _ in range(n+1)]
bvisited = [0 for _ in range(n+1)]
dans, bans = [], []
for i in range(n+1):
	paths[i] = sorted(paths[i])

def recur(cnt):
	dvisited[cnt] = 1
	dans.append(cnt)
	for i in paths[cnt]:
		if not dvisited[i]:
			recur(i)
recur(v)

que = deque([v])
bans.append(v)
bvisited[v] = 1
while que:
	top = que.popleft()
	for i in paths[top]:
		if not bvisited[i]:
			bvisited[i] = 1
			bans.append(i)
			que.append(i)
print(*dans)
print(*bans)