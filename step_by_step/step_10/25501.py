import sys
input = sys.stdin.readline

def recur(word, n):
	if not word or len(word) == 1:
		print(1, n)
	elif word[0] != word[-1]:
		print(0, n)
	else:
		recur(word[1:-1], n+1)


for _ in range(int(input())):
	s = input().split()
	recur(*s, 1)
