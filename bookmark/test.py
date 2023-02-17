from itertools import permutations
a,b,c,d = map(int, input().split())
arr_ = permutations([a,b,c,d], 4)
dis = 0
for i in arr_:
	arr = list(i)
	dis_ = abs(arr[0] - arr[1]) + abs(arr[2] - arr[3])
	dis = max(dis, dis_)

print(dis)