import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
	order = input().split()
	if order[0] == "push":
		lst.append(order[1])
	elif order[0] == "pop":
		if lst != []:
			print(lst.pop())
		else:
			print(-1)
	elif order[0] == "size":
		print(len(lst))
	elif order[0] == "empty":
		if lst == []:
			print(1)
		else:
			print(0)
	else:
		if lst == []:
			print(-1)
		else:
			print(lst[-1])
