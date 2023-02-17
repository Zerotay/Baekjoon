import sys

input = sys.stdin.readline
lst = [0] * 100
lst[0] = 1
lst[1] = 1
lst[2] = 1
lst[3] = 2
lst[4] = 2
for i in range(5, 100):
	lst[i] = lst[i - 1] + lst[i - 5]
for _ in range(int(input())):
	print(lst[int(input()) - 1])