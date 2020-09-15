from collections import Counter

#def frequency_sort(items):
    #my_list = []
    #counts = Counter(items)
    #my_list = sorted(items, key=lambda x: (counts[x], x), reverse=True)
    #print(sorted_keys)
    #return
    
def frequency_sort(items):
    items = sorted(items, key=lambda k:(items.count(k), -items.index(k)), reverse=True)
    return items

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    #assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    #assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    #assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    #assert list(frequency_sort([])) == []
    #assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([4,6,2,2,2,6,4,4,4])) == [4,4,4,4,2,2,2,6,6]
    assert list(frequency_sort([1,2,2,1])) == [1,1,2,2]
    print("Coding complete? Click 'Check' to earn cool rewards!")