def long_repeat(line):
    sum = 1
    sum_repeat = 0
    for i in range(len(line)-1):
        if line[i] == line[i + 1]:
            sum += 1
        else:
            sum = 1
        if sum > sum_repeat:
            sum_repeat = sum
    return sum_repeat

if __name__ == '__main__':
    assert long_repeat('abababaab') == 2, "first"
    assert long_repeat('ddvvrwwwrggg') == 3, "second"
    print('"Run" is good. How is "Check"?')