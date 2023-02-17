import heapq
n, k = map(int, input().split())
lst = [False] * 100002
que = [(0, n)]
while que:
	dist, top = heapq.heappop(que)
	lst[top] = True
	if top == k:
		print(dist)
		break
	if top*2 < 100002 and not lst[top*2]:
			heapq.heappush(que, (dist, top*2))
	if -1 < top-1 < 100002 and not lst[top-1]:
			heapq.heappush(que, (dist+1, top-1))
	if top+1 < 100002 and not lst[top+1]:
			heapq.heappush(que, (dist+1, top+1))