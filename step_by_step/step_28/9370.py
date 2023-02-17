import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
	lst = [inf] * (n+1)
	que = [(0,start)]
	lst[start] = 0
	while que:
		dist, now = heapq.heappop(que)
		if lst[now] < dist:
			continue
		for dest, weight in inlst[now]:
			cost = weight + dist
			if cost < lst[dest]:
				lst[dest] = cost
				heapq.heappush(que, (cost, dest))
	return lst

for _ in range(int(input())):
	n, m, t = map(int, input().split())
	s, g, h = map(int, input().split())
	inlst = [[] for _ in range(n+1)]
	for _ in range(m):
		n1, n2, v = map(int, input().split())
		inlst[n1].append((n2, v))
		inlst[n2].append((n1, v))
	possible = []
	for _ in range(t):
		possible.append(int(input()))
	possible.sort()
	from_s, from_g, from_h = dijkstra(s), dijkstra(g), dijkstra(h)
	for i in possible:
		through_path = min(from_s[g] + from_g[h] + from_h[i], \
							from_s[h] + from_h[g] + from_g[i])
		if through_path == from_s[i]:
			print(i, end=' ')
	print()
