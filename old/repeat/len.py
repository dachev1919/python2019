def my_len(mass):
	if mass == []:
		return 0
	else:
		return 1 + my_len(mass[1:])
if __name__ == "__main__":
	mass = [int(i) for i in input("Введие элементы списка через пробел: ").split()]
	print(my_len(mass))
