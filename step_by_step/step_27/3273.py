import sys
input = sys.stdin.readline

n = int(input())
inlst = [*map(int, input().split())]
x = int(input())
inlst.sort()
answer = 0

i1, i2 = 0, n-1
while i1 < i2:
	tmp = inlst[i1] + inlst[i2]
	if tmp < x:
		i1 += 1
	elif tmp > x:
		i2 -= 1
	else:
		answer += 1
		i1 += 1
		i2 -= 1

print(answer)