# Бинарный поиск числа
import time

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    step = 0

    while low <= high:
        step += 1
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            print("Мне понадобилось {} шагов".format(step))
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    value = int(input("Введите число, которое мне искать в отрезке от 0 до 100: "))
    start_time = time.perf_counter()
    my_list = []
    for i in range(100):
        my_list.append(i)

    print(binary_search(my_list, value))
    print("-----{} seconds-----".format(time.perf_counter() - start_time))
