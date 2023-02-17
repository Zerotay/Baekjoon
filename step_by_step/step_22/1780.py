import sys
input = sys.stdin.readline

def dc(x, y, n):
	global plus, zero, minus
	tmp = inlst[x][y]
	for i in range(x, x+n):
		for j in range(y, y+n):
			if tmp != inlst[i][j]:
				dc(x, y, n//3)
				dc(x + n//3, y, n//3)
				dc(x + n//3 * 2, y, n//3)
				dc(x, y + n//3, n//3)
				dc(x + n//3 , y + n//3, n//3)
				dc(x + n//3 * 2, y + n//3, n//3)
				dc(x, y + n//3 * 2, n//3)
				dc(x + n//3, y + n//3 * 2, n//3)
				dc(x + n//3 * 2, y + n//3 * 2, n//3)
				return
	if tmp == '1':
		plus += 1
	elif tmp == '0':
		zero += 1
	else:
		minus += 1


n = int(input())
inlst = [input().split() for _ in range(n)]
plus, zero, minus = 0, 0, 0
dc(0, 0, n)
print(minus, zero, plus, sep='\n')