import sys

input = sys.stdin.readline
string = input().rstrip()
q = int(input())
length = len(string)
lst = [[0] * 26]
for i in range(length):
	lst.append(lst[-1][:])
	lst[-1][ord(string[i]) - 97] += 1
for i in range(q):
	qt = list(input().rstrip().split())
	a, l, r = ord(qt[0]) - 97, int(qt[1]), int(qt[2])
	print(lst[r+1][a] - lst[l][a])