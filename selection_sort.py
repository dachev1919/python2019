
import time

def findSmallest(arr):              
    smallest = arr[0]               # для хранения наименьшего значения
    smallest_index = 0              # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    print(smallest_index)
    return smallest_index   

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == "__main__":
    start_time = time.perf_counter()
    print(selectionSort([9, 2, 3, 1, 4]))
    print("-----{} second-----".format(time.perf_counter() - start_time))
