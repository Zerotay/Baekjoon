import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
inlst = [[*map(int, input().split())] for _ in range(n + m)]
dic = {i[0]:i[1] for i in inlst}
lst = [0] * 101
que = deque([1])
while que:
	top = que.popleft()
	for i in range(6):
		nx = top + i + 1
		if nx < 101 and not lst[nx]:
			lst[nx] = lst[top] + 1
			j = nx
			while j in dic.keys():
				j = dic[j]
				if not lst[j]:
					lst[j] = lst[nx]
			que.append(j)
print(lst[100])
