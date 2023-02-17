import sys

input = sys.stdin.readline
print = sys.stdout.write

num = int(input().rstrip())
lst = [0 for _ in range(10000)]
for i in range(num):
	lst[int(input()) - 1] += 1
for i in range(10000):
	if lst[i] != 0:
		for j in range(lst[i]):
			print(str(i + 1) + "\n")
