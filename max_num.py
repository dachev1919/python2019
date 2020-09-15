# нахождение наибольшего числа
import time

def my_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = my_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

if __name__ == "__main__":
    start_time = time.perf_counter()
    print(my_max([1, 10, 3, 9, 6, 7]))
    print("----{} seconds----".format(time.perf_counter() - start_time))

