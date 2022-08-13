import sys

n = int(input())
lst = list(map(int, input().split()))
sum_lst = [0] * n

sum_lst[0] = lst[0]
for i in range(1, n):
	sum_lst[i] = max(lst[i], sum_lst[i - 1] + lst[i])
print(max(sum_lst))
