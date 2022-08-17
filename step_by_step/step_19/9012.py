import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
	string = list(input().rstrip())
	check = 0
	for i in range(len(string)):
		if string.pop() == ')':
			check += 1
		else:
			check -= 1
		if check < 0:
			break
	if check == 0:
		print("YES")
	else:
		print("NO")