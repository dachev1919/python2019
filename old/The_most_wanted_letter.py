def checkio(text: str) -> str:
    count = 0
    lower = text.lower()
    letter = lower[0]
    for i in lower:
        if i.isalpha():
            if lower.count(i) > count:
                count = lower.count(i)
                letter = i
            elif lower.count(i) == count and i < letter:
                letter = i
    return letter


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")