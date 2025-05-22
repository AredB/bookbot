def get_book_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_chars(text):
    lower_text = text.lower()
    chars = {
        "e": lower_text.count('e'),
        "t": lower_text.count('t'),
        "i": lower_text.count('i'),
        "n": lower_text.count('n'),
        "s": lower_text.count('s'),
        "r": lower_text.count('r'),
        "h": lower_text.count('h'),
        "d": lower_text.count('d'),
        "l": lower_text.count('l'),
        "m": lower_text.count('m'),
        "u": lower_text.count('u'),
        "c": lower_text.count('c'),
        "f": lower_text.count('f'),
        "y": lower_text.count('y'),
        "w": lower_text.count('w'),
        "p": lower_text.count('p'),
        "g": lower_text.count('g'),
        "b": lower_text.count('b'),
        "v": lower_text.count('v'),
        "k": lower_text.count('k'),
        "x": lower_text.count('x'),
        "j": lower_text.count('j'),
        "q": lower_text.count('q'),
        "z": lower_text.count('z'),
        "æ": lower_text.count('æ'),
        "â": lower_text.count('â'),
        "ê": lower_text.count('ê'),
        "ë": lower_text.count('ë'),
        "ô": lower_text.count('ô')
    }
    return chars

def get_sorted_chars(chars):
    list = []
    report = ""
    for i in chars:
        list.append({"char": i, "num": chars[i]})
    for item in list:
        report += f"{item["char"]}: {item["num"]}\n"
    return report

def sort_on(chars):
    return chars["num"]