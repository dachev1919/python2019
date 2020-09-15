import random
def check(x):
	b = []
	c = 0
	a = 0
	while c != x:
		a+=1
		c = random.randint(1000, 99999)
		if c not in b:
			b.append(c)
	print("Нам потребовалось ", a, "попыток.")
	return c

if __name__ == "__main__":
	x = int(input(u"Введите пасс из 4 чесел(число не меньше 1000): "))
	print("Вы загадали число ", check(x))