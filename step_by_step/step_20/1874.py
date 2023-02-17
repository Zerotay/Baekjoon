import sys
input = sys.stdin.readline

n = int(input())
inlst = []
numlst = [i for i in range(1, n+1)]
stack = [0]
answer = []
for _ in range(n):
	inlst.append(int(input()))
curr = 0
for i in range(1, n+1):
	stack.append(i)
	answer.append('+')
	while curr < n and inlst[curr] == stack[-1]:
		stack.pop()
		answer.append('-')
		curr += 1
if stack == [0]:
	print(*answer, sep='\n')
else:
	print("NO")
