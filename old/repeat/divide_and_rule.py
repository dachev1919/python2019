def summ(mass):
	"""text"""
	if mass == []:
		return 0
	else:
		return mass[0] + summ(mass[1:])

if __name__ == "__main__":
	mass = [int(i) for i in input("Введие элементы списка через пробел: ").split()]
	print(summ(mass))