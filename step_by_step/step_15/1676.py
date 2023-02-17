n = int(input())
answer = 0
for i in range(5,n + 1,5):
	while i % 5 == 0:
		i //= 5
		answer += 1
print(answer)