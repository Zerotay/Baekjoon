import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
	p = input().rstrip()
	n = int(input())
	inlst =deque(input().strip("[]\n").split(','))
	if n == 0:
		inlst = deque()
	rotate = 0
	flag = 0
	for i in range(len(p)):
		if p[i] == "R":
			rotate += 1
		elif p[i] == "D":
			if not inlst:
				print("error")
				flag = 1
				break
			if rotate % 2:
				inlst.pop()
			else:
				inlst.popleft()
	if rotate % 2:
		inlst.reverse()
	if not flag:
		print('['+','.join(inlst)+']')