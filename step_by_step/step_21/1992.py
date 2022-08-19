import sys
input = sys.stdin.readline

def dc(x, y, n):
	global answer
	tmp = inlst[x][y]
	for i in range(x, x+n):
		for j in range(y, y+n):
			if tmp != inlst[i][j]:
				answer.append('(')
				dc(x, y, n//2)
				dc(x, y + n//2, n//2)
				dc(x + n//2, y, n//2)
				dc(x + n//2, y + n//2, n//2)
				answer.append(')')
				return
	if tmp == '0':
		answer.append('0')
	else:
		answer.append('1')

n = int(input())
inlst = [input().rstrip() for _ in range(n)]
answer = []
dc(0,0,n)
print(''.join(answer))
