from collections import deque

n, k = map(int, input().split())
lst = deque(i for i in range(1, n+1))
answer = []
while lst:
	lst.rotate(-k+1)
	answer.append(lst.popleft())
print('<' + ', '.join(map(str, answer)) + '>')