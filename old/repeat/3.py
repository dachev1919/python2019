def YorikOleg(value, text):
	count = 0
	while count != value:
		print(text)
		count += 1
def main():
	value = int(input("Склолько раз будем повторять: "))
	text = input("Какой текст будем повторять: ")
	YorikOleg(value, text)

if __name__ == "__main__":
	main()
	input("Press enter for EXIT...")