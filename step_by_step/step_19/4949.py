import sys

input = sys.stdin.readline
while True:
	string = list(input().rstrip())
	if string == ["."]:
		break
	lst = []
	check = True
	for i in string:
		if i in ["(","["]:
			lst.append(i)
		elif i == ')':
			if not lst or lst[-1]  == '[':
				check = False
				break
			elif lst[-1] == '(':
				lst.pop()
			else:
				lst.append(i)
		elif i == ']':
			if not lst or lst[-1]  == '(':
				check = False
				break
			elif lst[-1] == '[':
				lst.pop()
			else:
				lst.append(i)
	if check and not lst:
		print('yes')
	else:
		print('no')