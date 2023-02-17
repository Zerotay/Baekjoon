import sys

input = sys.stdin.readline
lst = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def dp(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	elif a > 20 or b > 20 or c > 20:
		return dp(20, 20, 20)
	elif lst[a][b][c] != 0:
		return lst[a][b][c]
	elif a < b and b < c:
		lst[a][b][c] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a, b-1, c)
		return lst[a][b][c]
	else :
		lst[a][b][c] = dp(a-1, b, c) + dp(a-1, b-1, c) + dp(a-1, b, c-1) - dp(a-1, b-1, c-1)
		return lst[a][b][c]

while True:
	a, b, c = map(int, input().split())
	if a == -1 and b == -1 and c == -1:
		break
	print(f'w({a}, {b}, {c}) = {dp(a,b,c)}')
