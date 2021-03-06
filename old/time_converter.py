def time_converter(time):
    if int(time[:-3]) < 1:
        return "12" + time[2:] + " a.m."
    elif int(time[:-3]) <= 12:
        if int(time[:-3]) < 10:
            return time[1:] + ' a.m.'
        return time + ' p.m.'
    else:
        i = int(time[:-3]) - 12
        return str(i) + time[2:] + ' p.m.'

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")