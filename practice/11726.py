n = int(input())
lst = [0 for _ in range(1000)]
lst[0] = 1
lst[1] = 2

def recur(k):
	if lst[k]: return lst[k]
	lst[k] = recur(k-1) + recur(k-2)
	return lst[k]

print(recur(n-1) % 10007)


# n = int(input())
# lst = [0 for _ in range(1000)]
# lst[0] = 1
# lst[1] = 2
# for i in range(2,1000): lst[i] = lst[i-2] + lst[i-1]
# print(lst[n-1] % 10007)