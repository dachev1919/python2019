def checkio(data: list) -> list:
    main_list = []
    for i in data:
        count = 0
        for j in range(len(data)):
            if i == data[j]:
                count += 1
                if count == 2:
                    main_list.append(i)
    return main_list
if __name__ == "__main__":
	assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
	assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
	assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
	print("It is all good. Let's check it now")