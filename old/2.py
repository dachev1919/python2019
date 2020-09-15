value = input()
my_list = []
count = 0
length = len(value)
if length % 2 != 0:
	count += 1
else:
	count = 0
a = 0
b = (-1)
for i in value:
	my_list.append(i)
for i in my_list:
	a += 1
	if length//2 < a:
		break
	if i == my_list[b]:
		count += 1
	b -= 1
print(count)