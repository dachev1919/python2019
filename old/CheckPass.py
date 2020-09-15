count = 0
while count != 1:
	password = input('Enter password to check for difficult: ')
	if len(password) > 10:
		if any(c.isupper() for c in password):
			if any(map(str.isdigit, password)):
				count += 1
	else:
		print("Password is easy")
print("Thats good password")