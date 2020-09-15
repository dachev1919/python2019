def to_encrypt(text, delta):
    list(text)
    new_text = []
    for letter in text:
        if not letter.isalpha():
            new_text.append(letter)
            continue
        if ord(letter) + delta > 122:
            new_letter = chr(96 + (delta - (122 - ord(letter))))
        elif ord(letter) + delta < 97:
            new_letter = chr(ord(letter) + (26 + delta))
        else:
            new_letter = chr(ord(letter) + delta)
        new_text.append(new_letter)
    return "".join(new_text)

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")