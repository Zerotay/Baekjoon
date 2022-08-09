import sys

def get_key(k):
	for key, value in nlst.items():
		if k == value:
			return int(key) + 1

input = sys.stdin.readline
n, m = map(int, input().split())
nlst = {i : input().rstrip("\n") for i in range(n)}
rev_nlst = dict(map(reversed, nlst.items()))
mlst = [input().rstrip("\n") for _ in range(m)]
for i in mlst:
	if i.isdigit() == True:
		print(nlst[int(i) - 1])
	else:
		print(rev_nlst[i] + 1)