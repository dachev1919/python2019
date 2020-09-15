def find_max_num(mass):
	"""function find max num(created by the author)"""
	if len(mass) == 2:
		return mass[0] if mass[0] > mass[1] else mass[1]

	sub_max = find_max_num(mass[1:])
	return list[0] if list[0] > sub_max else sub_max

def find_max(mass, maximum):
	"""function find max number(Created by me)"""
	if mass != [] and mass[0] > maximum:
		maximum = mass[0]

	if mass == []:
		return maximum
	else:
		return find_max(mass[1:], maximum)

if __name__ == "__main__":
	mass = [int(i) for i in input("Введите числа через пробел: ").split()]
	maximum = 0
	print(find_max_num(mass))