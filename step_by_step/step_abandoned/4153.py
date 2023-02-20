import sys

input = sys.stdin.readline

while True:
	x, y, z = map(int, input().split())
	if x == 0 and y == 0 and z == 0:
		break
	lst = [i ** 2 for i in [x,y,z]]
	if max(lst) == sum(lst) - max(lst):
		print("right")
	else:
		print("wrong")
