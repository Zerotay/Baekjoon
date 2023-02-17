import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
inlst = [[] for _ in range(v+1)]
for _ in range(e):
	s, e, d = map(int, input().split())
	inlst[s].append([e, d])

inf = sys.maxsize
shortest = [inf] * (v+1)

def dijkstra():
	que = []
	heapq.heappush(que, (0, start))
	shortest[start] = 0
	while que:
		dist, node = heapq.heappop(que)
		if shortest[node] < dist:
			continue
		for i in inlst[node]:
			cost = dist + i[1]
			if cost < shortest[i[0]]:
				shortest[i[0]] = cost
				heapq.heappush(que, (cost, i[0]))

dijkstra()
for i in shortest[1:]:
	print("INF" if i == inf else i)