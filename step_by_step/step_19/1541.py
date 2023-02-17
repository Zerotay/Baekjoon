inlst = input()
lst = inlst.split("-")
for i in range(len(lst)):
	if "+" in lst[i]:
		lst[i] = lst[i].split("+")
		lst[i] = sum(list(map(int, lst[i])))
	else:
		lst[i] = int(lst[i])
answer = lst[0] * 2
for i in lst:
	answer -= i
print(answer)