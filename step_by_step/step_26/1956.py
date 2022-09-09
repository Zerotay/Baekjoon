import sys
import heapq as hq
input = sys.stdin.readline
inf = sys.maxsize

v, e = map(int, input().split())
inlst = [[] for _ in range(v+1)]
lst = [[inf] * (v+1) for _ in range(v+1)]
que = []
for _ in range(e):
	a,b,c = map(int, input().split())
	inlst[a].append((b,c))
	lst[a][b] = c
	hq.heappush(que, [c, a, b])

while que:
	dist, start, end = hq.heappop(que)
	if start == end:
		print(dist)
		exit(0)
	if lst[start][end] < dist:
		continue
	for nnext, ndist in inlst[end]:
		cost = ndist + dist
		if cost < lst[start][nnext]:
			lst[start][nnext] = cost
			hq.heappush(que, [cost, start, nnext])
else:
	print(-1)