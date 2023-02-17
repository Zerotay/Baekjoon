import sys

input = sys.stdin.readline
print = sys.stdout.write
lst = []
for i in range(int(input())):
	lst.append(int(input().rstrip()))
lst.sort()
for i in lst:
	print(str(i) + "\n")