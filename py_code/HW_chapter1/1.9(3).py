list1 = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(list1)):
	for j in list1[i]:
		print("{0},\t".format(j))
	print("\n")