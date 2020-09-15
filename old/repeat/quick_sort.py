
#dasdasdas
def my_len(array):
	list
	if array == []:
		return 0
	else:
		return 1 + my_len(array[1:])

def quick_sort(array):
	if my_len(array) < 2:
		return array
	else:
		mid = my_len(array) // 2
		less = [i for i in array[:mid] + array[mid+1:] if i <= mid]
		greater = [i for i in array[:mid] + array[mid+1:] if i > mid]
		return quick_sort(less) + [array[mid]] + quick_sort(greater)

if __name__ == "__main__":
	array = [int(i) for i in input("Введите числа через запятую: ").split()]
	print(quick_sort(array))