from collections import deque

n, m = map(int, input().split())
inlst = list(map(int, input().split()))
lst = deque(i + 1 for i in range(n))
answer = 0
for i in inlst:
	while True:
		if i == lst[0]:
			lst.popleft()
			break
		elif lst.index(i) <= len(lst) // 2:
			while i != lst[0]:
				lst.rotate(-1)
				answer += 1
		else :
			while i != lst[0]:
				lst.rotate(1)
				answer += 1
print(answer)
