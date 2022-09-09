import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

n, e = map(int, input().split())
inlst = [[] for _ in range(n+1)]
for _ in range(e):
	s, e, d = map(int, input().split())
	inlst[s].append((e, d))
	inlst[e].append((s, d))
v1, v2 = map(int, input().split())

def dijkstra(start):
	lst = [inf] * (n+1)
	que = [(0, start)]
	lst[start] = 0
	while que:
		dist, node = heapq.heappop(que)
		if lst[node] < dist:
			continue
		for i in inlst[node]:
			cost = dist + i[1]
			if cost < lst[i[0]]:
				lst[i[0]] = cost
				heapq.heappush(que, (cost, i[0]))
	return lst

a, b, c = dijkstra(1), dijkstra(v1), dijkstra(v2)
answer = min(a[v1] + b[v2] + c[n], a[v2] + c[v1] + b[n])
print(-1 if answer >= inf else answer)