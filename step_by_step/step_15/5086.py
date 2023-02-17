import sys

input = sys.stdin.readline
while True:
	n, m = map(int, input().split())
	if not n and not m:
		break
	if max(n, m) % min(n, m):
		print("neither")
	elif n > m:
		print("multiple")
	else:
		print("factor")