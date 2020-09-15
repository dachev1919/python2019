def flat_list(array):
    array = list(function(array))
    return array

def function(array):
    for x in array:
        if isinstance(x, list):
            yield from function(x)
        else:
            yield x

if __name__ == '__main__':
    main_list = []
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], print("Second")
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"

    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')