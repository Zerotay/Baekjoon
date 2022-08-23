import sys
input = sys.stdin.readline
from collections import deque

while True:
	string = deque(map(int, input().split()))
	n = string.popleft()
	if not n:
		break
	lst = []
	answer = 0
	for i in range(n):
		while lst and string[lst[-1]] > string[i]:
			tmp = lst.pop()
			if not lst:
				width = i
			else:
				width = i - lst[-1] - 1
			answer = max(answer, width * string[tmp])
		lst.append(i)
	while lst:
		tmp = lst.pop()
		if not lst:
			width = n
		else:
			width = n - lst[-1] - 1
		answer = max(answer, width * string[tmp])
	print(answer)
