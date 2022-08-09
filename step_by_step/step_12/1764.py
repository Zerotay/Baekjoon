import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nset = set(input().rstrip() for _ in range(n))
mset = set(input().rstrip() for _ in range(m))
result = sorted(nset & mset)
print(len(result))
for i in result:
	print(i)
