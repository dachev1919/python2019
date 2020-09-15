def check_voted(dictionary, name):
	if dictionary.get(name):
		return print("Вы уже присутствуете в наших списках, и не имеете право голосовать")
	else:
		vote = input("Введите ваш голос: ")
		dictionary[name] = vote
		return dictionary

if __name__ == "__main__":
	dictionary = dict()
	name = input("Введите ваше имя(мы проверим на наличие в списках): ")
	print(check_voted(dictionary, name))