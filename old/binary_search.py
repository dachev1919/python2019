def binary_search(list, item):
	""" Fuction binary search """
	low = 0
	high = len(list)-1
	step = 0
	found = False

	while low <= high and not found:
		step += 1
		print("step number -> ", step)

		mid = (low + high) // 2
		if list[mid] == item:
			found = True
		else:
			if item < list[mid]:
				high = mid-1
			else:
				low = mid+1

	return found

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(my_list, 6))
print(binary_search(my_list, -1))