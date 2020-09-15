def greet(name):
	print("hello, " + name + "!")
	greet2(name)
	bye(name)
	
def greet2(name):
	print("How are you, " + name + "?\n"
		  + "Getting ready to say bye..")
	
def bye(name):
	print("Okey, bye " + name)

if __name__ == "__main__":
	name = input(u"Введите свое имя: ")
	greet(name)