import sys
import math

def incircle(circle, x, y):
	if math.hypot(circle[0] - x, circle[1] - y) < circle[2]:
		return True
	return False

input = sys.stdin.readline

for _ in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())
	n = int(input())
	lst = []
	answer = 0
	for i in range(n):
		lst.append(list(map(int, input().split())))
	for i in lst:
		stpt = incircle(i, x1, y1)
		enpt = incircle(i, x2, y2)
		if (stpt and enpt) or (stpt == False and enpt == False):
			pass
		else:
			answer += 1
	print(answer)
