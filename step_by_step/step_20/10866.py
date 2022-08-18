from collections import deque
import sys
input = sys.stdin.readline
lst = deque()
for _ in range(int(input())):
	order = input().split()
	if order[0] == 'push_front':
		lst.appendleft(int(order[1]))
	elif order[0] == 'push_back':
		lst.append(int(order[1]))
	elif order[0] == 'pop_front':
		if not lst:
			print(-1)
		else:
			print(lst.popleft())
	elif order[0] == 'pop_back':
		if not lst:
			print(-1)
		else:
			print(lst.pop())
	elif order[0] == 'size':
		print(len(lst))
	elif order[0] == 'empty':
		if not lst:
			print(1)
		else:
			print(0)
	elif order[0] == 'front':
		if not lst:
			print(-1)
		else:
			print(lst[0])
	elif order[0] == 'back':
		if not lst:
			print(-1)
		else:
			print(lst[-1])