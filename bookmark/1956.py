import sys
import heapq as hq
input = sys.stdin.readline
inf = sys.maxsize

v, e = map(int, input().split())
lst = [[inf] * (v+1) for _ in range(v+1)]
que = []
inlst = [[] for _ in range(v+1)]
for _ in range(e):
	s, e, d = map(int, input().split())
	inlst[s].append((e, d))
	lst[s][e] = d
	hq.heappush(que, (d, s, e))

while que:
	dist, start, end = hq.heappop(que)
	if start == end:
		print(dist)
		exit(0)
	if lst[start][end] < dist: continue
	for i, j in inlst[end]:
		cost = dist + j
		if cost < lst[start][i]:
			lst[start][i] = cost
			hq.heappush(que, (cost, start, i))
else: print(-1)