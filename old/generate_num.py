def gen_num(n:int, m:int, prefix=None):
    """ Generate numbers """
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for digit in range(n):
        prefix.append(digit)
        generate_num(n, m-1, prefix)
        prefix.pop()
if __name__ == "__main__":
    generate_num(2, 3)