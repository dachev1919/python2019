import time
def insert_sort(list):
	""" Cортировка списка методом вставки """
	n = len(list)
	for top in range(1, n):
		k = top
		while k > 0 and list[k - 1] > list[k]:
			list[k], list[k - 1] = list[k - 1], list[k]
			k -= 1
	return list

def choice_sort(list):
	""" Cортировка списка методом выбора """
	n = len(list)
	for pos in range(0 , n - 1):
		for k in range(pos + 1, n):
			if list[k] < list[pos]:
				list[k], list[pos] = list[pos], list[k]
	return list

def bubble_sort(list):
	""" Cортировка списка пузырьковым методом """
	n = len(list)
	for bypass in range(1, n):
		for k in range(0, n - bypass):
			if list[k] > list[k + 1]:
				list[k], list[k + 1] = list[k + 1], list[k]
	return list

if __name__ == "__main__":
	list = list(range(99, 1, -1))
	for f in insert_sort, choice_sort, bubble_sort:
		start_time = time.time()
		print(f.__doc__)
		f(list)
		print("--- %s seconds ---" % (time.time() - start_time))
	