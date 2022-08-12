n = int(input())
lst = [-1 for _ in range(n)]
answer = 0

def check(curr):
	for i in range(curr):
		if curr - i == abs(lst[i] - lst[curr]) or lst[i] == lst[curr]:
			return False
	return True

def nqueen(floor):
	global answer
	if floor == n:
		answer += 1
		return
	elif floor == 0:
		i = 0
		while i < n // 2:
			lst[floor] = i
			if check(floor):
				nqueen(floor + 1)
			i += 1
		answer *= 2
		if n % 2 == 1:
			lst[floor] = i
			if check(floor):
				nqueen(floor + 1)
	else:
		for i in range(n):
			lst[floor] = i
			if check(floor):
				nqueen(floor + 1)

nqueen(0)
print(answer)