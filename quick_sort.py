# Алгоритм быстрой сортировки
import random
import time

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    start_time = time.perf_counter()
    print(quick_sort([1, 3, 2, 4, 8, 10]))
    print(time.perf_counter() - start_time, "seconds")

