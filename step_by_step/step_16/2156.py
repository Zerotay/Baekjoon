import sys

input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
if n == 1:
	print(lst[0])
	exit(0)
elif n == 2:
	print(lst[0] + lst[1])
	exit(0)
max_lst = [0 for _ in range(10001)]
max_lst[0] = lst[0]
max_lst[1] = lst[0] + lst[1]
max_lst[2] = max(max_lst[1], max_lst[0] + lst[2], lst[2] + lst[1])
for i in range(3, n):
	max_lst[i] = max(max_lst[i-1], max_lst[i-2] + lst[i], max_lst[i-3] + lst[i] + lst[i-1])

print(max_lst[n-1])