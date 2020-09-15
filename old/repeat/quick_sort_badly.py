def quick_sort(array):
	if len(array) < 2:
		return array
	else:
		mid = array[0]
		less = [i for i in array[1:] if i <= mid]
		greater = [i for i in array[1:] if i > mid]
		return quick_sort(less) + [mid] + quick_sort(greater)
if __name__ == "__main__":
	array = [int(i) for i in input(u"Введите числа, которые войдут в список(через пробел): ").split()]
	print(quick_sort(array))