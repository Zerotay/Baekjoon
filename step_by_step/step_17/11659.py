import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = [0, lst[0]]
for i in range(1, n):
	sum_lst.append(sum_lst[i] + lst[i])
for _ in range(m):
	s, e = map(int, input().split())
	print(sum_lst[e] - sum_lst[s-1])