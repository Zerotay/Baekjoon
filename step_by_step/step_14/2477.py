import sys

input = sys.stdin.readline
n = int(input())
shape = []
lst = [0,0,0,0]
for i in range(6):
	x, y = map(int, input().split())
	shape.append([x,y])
max_x = max(shape[0::2], key=lambda x: x[1])
max_y = max(shape[1::2], key=lambda x: x[1])

if shape.index(max_x) == 0:
	if shape.index(max_y) == 1:
		small_x = shape[shape.index(max_x) + 4]
		small_y = shape[shape.index(max_y) + 2]
	else:
		small_x = shape[shape.index(max_x) + 2]
		small_y = shape[shape.index(max_y) - 2]
elif shape.index(max_x) == 2:
	if shape.index(max_y) == 3:
		small_x = shape[shape.index(max_x) - 2]
		small_y = shape[shape.index(max_y) + 2]
	else:
		small_x = shape[shape.index(max_x) + 2]
		small_y = shape[shape.index(max_y) + 4]
else:
	if shape.index(max_y) == 5:
		small_x = shape[shape.index(max_x) - 2]
		small_y = shape[shape.index(max_y) - 4]
	else:
		small_x = shape[shape.index(max_x) - 4]
		small_y = shape[shape.index(max_y) - 2]

print(((max_x[1] * max_y[1]) - (small_x[1] * small_y[1])) * n)

#본받을 코드
# r=[4,3,1,2]
# N=int(input())
# L=[]
# X=0
# Y=0
# S=0
# m2=0
# for i in range(6):
#     s,d=map(int,input().split())
#     if i!=0:
#         if r[S-1]!=s:
#             m1=d
#             m2=L[-1]
#     L+=[d]
#     S=s
#     if (s==1 or s==2) and d>X:X=d
#     if (s==3 or s==4) and d>Y:Y=d
# if m2==0:
#     m1=L[0]
#     m2=L[-1]
# print(N*(X*Y-m1*m2))
