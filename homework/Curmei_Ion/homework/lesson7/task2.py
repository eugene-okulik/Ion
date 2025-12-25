words = {"I": 3, "love": 5, "python": 1, "!": 50}


def multipy_item(words):
    for key, value in words.items():
        print(value * key)


multipy_item(words)
