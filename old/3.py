num = bin(int(input()))
print(num)
my_list = []
my_list_test = []
result = []
count = 0

for i in num:
	my_list.append(i)
	my_list_test.append(i)
del my_list[0:2], my_list_test[0:2]

for i in my_list:
	my_list_test.append(i)
	del my_list_test[0]
	if count < len(my_list_test):
		test = ''.join(map(str, my_list_test))
		number = int(test, 2)
		result.append(number)
	else:
		break

result = sorted(result)
print("Все получившиеся числа: ", result)
print("Наибольшее число:", result[-1])
