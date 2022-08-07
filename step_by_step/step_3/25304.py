cost = (int)(input())
num = (int)(input())
lst = []
for i in range(num):
	tmp = list(input().split(" "))
	lst.append(tmp)
answer = 0
for i in lst:
	answer += int(i[0]) * int(i[1])
if answer == cost:
	print("Yes")
else:
	print("No")