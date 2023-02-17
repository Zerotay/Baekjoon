import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
inlst = [[inf] * n for _ in range(n)]
for _ in range(m):
	a, b, c = map(int, input().split())
	inlst[a-1][b-1] = min(inlst[a-1][b-1], c)
for i in range(n):
	inlst[i][i] = 0

for i in range(n):
	for j in range(n):
		for k in range(n):
			inlst[j][k] = min(inlst[j][k], inlst[j][i] + inlst[i][k])
for i in inlst:
	for j in i:
		print(j if j != inf else 0, end=' ')
	print()

# 플워를 활용하는 문제이지만, 다익스트라를 응용해서도 풀 수 있다.
# 시간은 더 느리다.
# import sys
# input = sys.stdin.readline
# import heapq as hq
# inf = sys.maxsize

# n = int(input())
# m = int(input())
# inlst = [[] for _ in range(n+1)]
# lst = [[inf] * (n+1) for _ in range(n+1)]
# que = []
# for _ in range(m):
# 	a, b, c = map(int, input().split())
# 	inlst[a].append((b,c))
# 	lst[a][b] = min(lst[a][b], c)
# 	hq.heappush(que, (c, a, b))

# for i in range(n+1):
# 	lst[i][i] = 0

# while que:
# 	dist, start, end = hq.heappop(que)
# 	if lst[start][end] < dist:
# 		continue
# 	for nnext, ndist in inlst[end]:
# 		cost = dist + ndist
# 		if cost < lst[start][nnext]:
# 			lst[start][nnext] = cost
# 			hq.heappush(que, (cost, start, nnext))
# for i in lst[1:]:
# 	for j in i[1:]:
# 		print(j if j != inf else 0, end=' ')
# 	print()