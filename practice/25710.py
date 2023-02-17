from itertools import combinations_with_replacement as cwr
from collections import Counter

n = int(input())
inlst = Counter(map(int, input().split()))
ans = 0
for i, j in cwr(inlst, 2):
	if i != j or inlst[i] > 1:
		ans = max(ans, sum(map(int, str(i*j))))
print(ans)
