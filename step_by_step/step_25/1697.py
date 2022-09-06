from collections import deque
n, k = map(int, input().split())
lst = [0] * 100002
que = deque([n])
while True:
	top = que.popleft()
	if top == k:
		print(lst[top])
		break
	for i in (top-1, top+1, top*2):
		if -1 < i < 100002 and not lst[i]:
			lst[i] = lst[top] + 1
			que.append(i)