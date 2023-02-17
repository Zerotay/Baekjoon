import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
inlst = [[] for _ in range(n+1)]
for i in range(m):
	s, e = map(int, input().split())
	inlst[s].append(e)

lst = [-1 for _ in range(n+1)]
lst[x] = 0
que = deque()
que.append(x)
while que:
	node = que.popleft()
	if lst[node] > k: continue
	for i in inlst[node]:
		if lst[i] == -1:
			lst[i] = lst[node] + 1
			que.append(i)
ans = []
for i in range(1, n+1):
	if lst[i] == k: ans.append(i)
if ans: print(*ans, sep='\n')
else: print(-1)