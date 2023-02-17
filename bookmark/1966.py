from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
	n, m = map(int,input().split())
	inlst = map(int, input().split())
	lst = deque((j,i) for i, j in enumerate(inlst))
	count = 0
	while True:
		if max(lst)[0] == lst[0][0]:
			count += 1
			tmp = lst.popleft()
			if tmp[1] == m:
				print(count)
				break
		else: lst.rotate(-1)
