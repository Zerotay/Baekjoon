from collections import deque
import enum
import sys
input = sys.stdin.readline

for _ in range(int(input())):
	lst = []
	n, m = map(int, input().split())
	inlst = list(map(int, input().split()))
	lst = deque((val, i) for i, val in enumerate(inlst))
	answer = 0
	while True:
		if max(lst)[0] == lst[0][0]:
			k = lst.popleft()
			answer += 1
			if k[1] == m:
				print(answer)
				break
		else:
			lst.append(lst.popleft())