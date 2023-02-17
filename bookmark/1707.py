import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
	v, e = map(int, input().split())
	inlst = [[] for _ in range(v+1)]
	for _ in range(e):
		n1, n2 = map(int, input().split())
		inlst[n1].append(n2)
		inlst[n2].append(n1)
	check = [0 for _ in range(v+1)]
	que = deque()
	answer = True
	for i in range(1, v+1):
		if not check[i]:
			que.append(i)
			check[i] = 1
			while que:
				node = que.popleft()
				for j in inlst[node]:
					if not check[j]:
						que.append(j)
						check[j] = -check[node]
					elif check[node] == check[j]:
						answer = False
						break
	print('YES' if answer else 'NO')
