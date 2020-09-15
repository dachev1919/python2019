def matryoshka(n):
	""" Рекурсия """
	if n == 1:
		print("Матрёшечка")
	else:
		print("Верх матрёшечки", n)
		matryoshka(n - 1)
		print("Низ матрёшечки", n)

if __name__ == "__main__":
	matryoshka(5)