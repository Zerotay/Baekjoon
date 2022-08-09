import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nlst = {input().rstrip("\n") for i in range(n)}
mlst = [input().rstrip("\n") for i in range(m)]
answer = 0
for i in mlst:
	if i in nlst:
		answer += 1
print(answer)