if __name__ == "__main__":
	value = int(input("Сколько раз повторить: "))
	text = input("Введите текст для повторения:")
	count = 0
	while count != value:
		print(text)
		count += 1
