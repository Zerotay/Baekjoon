import sys
input = sys.stdin.readline

for _ in range(int(input())):
	inlst = input().rstrip()
	for _ in range(25): inlst = inlst.replace('()', '')
	if inlst: print('NO')
	else: print('YES')
