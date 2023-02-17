from collections import Counter

for _ in range(int(input())):
	lst = []
	for _ in range(int(input())):
		lst.append(list(input().split())[1])
	count = Counter(lst)
	k = list(count)
	answer = 1
	for i in range(len(k)):
		answer *= count[k[i]] + 1
	print(answer - 1)