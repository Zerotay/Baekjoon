import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
paths = {i:set() for i in range(n+1)}
for _ in range(int(input())):
	s, e = map(int, input().split())
	paths[s].add(e)
	paths[e].add(s)
visited = [0 for _ in range(n+1)]
que = deque([1])
visited[1] = 1
answer = 0
while que:
	top = que.popleft()
	for i in paths[top]:
		if not visited[i]:
			visited[i] = 1
			answer += 1
			que.append(i)
print(answer)