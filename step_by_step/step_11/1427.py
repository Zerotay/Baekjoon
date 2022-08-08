lst = [i for i in input()]
lst.sort(reverse=True)
answer = ''
for i in lst:
	answer += i
print(answer)