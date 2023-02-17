import sys

input = sys.stdin.readline
n = int(input())
lst = [0 for _ in range(301)]
score = [0 for _ in range(301)]
for i in range(n):
	lst[i] = int(input())
score[0] = lst[0]
score[1] = lst[0] + lst[1]
score[2] = lst[2] + max(lst[0], lst[1])
for i in range(3, n):
	score[i] = lst[i] + max(lst[i-1] + score[i-3], score[i-2])
print(score[n-1])