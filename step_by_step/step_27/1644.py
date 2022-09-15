n = int(input())
eratos = [1 for _ in range(4000_000)]
eratos[0] = eratos[1] = 0
for i in range(2, 2000):
	j = i
	if eratos[j]:
		j += i
		while j < 4000_000:
			eratos[j] = 0
			j += i
lst = [i for i in range(4000000) if eratos[i]]
i1 = i2 = 0
ans = 0
tmp = lst[i1]
while i1 < n:
	if tmp < n:
		if i2 == len(lst) - 1:
			break
		i2 += 1
		tmp += lst[i2]
	elif tmp > n:
		tmp -= lst[i1]
		i1 += 1
	else:
		ans += 1
		tmp -= lst[i1]
		i1 += 1
print(ans)