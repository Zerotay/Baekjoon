import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
	v, e = map(int, input().split())
	path = [[] for _ in range(v+1)]
	for _ in range(e):
		s, d = map(int, input().split())
		path[s].append(d)
		path[d].append(s)
	visited = [0 for _ in range(v+1)]
	que = deque()
	answer = True
	for i in range(1, v+1):
		if not visited[i]:
			que.append(i)
			visited[i] = 1
			while que:
				top = que.popleft()
				for j in path[top]:
					if not visited[j]:
						que.append(j)
						visited[j] = -visited[top]
					elif visited[j] == visited[top]:
						answer = False
						break
	print("YES" if answer else "NO")