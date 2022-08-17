import sys

input = sys.stdin.readline
k = int(input())
lst = []
for i in range(k):
	tmp = int(input())
	if tmp == 0:
		lst.pop()
	else:
		lst.append(tmp)
print(sum(lst))
