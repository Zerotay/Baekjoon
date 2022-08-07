from collections import Counter
import sys

lst = []
n = int(input())
for i in range(n):
	lst.append(int(sys.stdin.readline()))
lst.sort()
count = Counter(lst)
print(round(sum(lst) / n))
print(lst[(n - 1) // 2])
i = 1 if n != 1 and count.most_common()[0][1] == count.most_common()[1][1] else 0
print(count.most_common(2)[i][0])
print(lst[n - 1] - lst[0])
