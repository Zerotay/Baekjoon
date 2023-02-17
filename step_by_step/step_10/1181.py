lst = []
for _ in range(int(input())):
	lst.append(input())
rmdup = sorted(set(lst), key= lambda x: (len(x), x))
print(*rmdup, sep="\n")