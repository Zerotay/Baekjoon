lst = list(map(lambda x : int(x), list(input().split(" "))))
default = [1,1,2,2,2,8]
for a, b in zip(lst, default):
	print(b - a, end=" ")