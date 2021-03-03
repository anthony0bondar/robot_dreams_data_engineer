import string


def run():
    print(string.punctuation)
    print(string.octdigits)
    print(string.printable)
    print()


    p_string = "Some python string"

    # strings in Python are immutable objects
    s_str = "String 0"
    s_str2 = "String 0"
    print(id(s_str))
    print(id(s_str2))

    print(id(s_str))
    s_str += "1"
    print(id(s_str))
    print()

    # access characters as in a list
    print(p_string[0])
    print()

    # iterate over string
    for ch in p_string:
        print(ch, end='')
    print()
    print()

    # if string contains substring
    print('python' in p_string)
    print('Python' in p_string)
    print()

    # string length
    print(len(p_string), end=" - number of characters in the string\n")
    print()

    # string formatting
    languages = ['Python', 'Java', 'Scala', 'R']
    word = "My"
    for language in languages:
        print("{} favorite programming language is {}".format(word, language))
    for language in languages:
        print(f"{word} favorite programming language is {language}")
    print()

    # split string into substrings and join back
    words_list = p_string.split(' ')
    print(words_list)
    print('_'.join(words_list))
    print()

    # split string on line breaks
    # and removing whitespaces from both ends of a line
    sentence = """
    Very long
    but simple
    Python string
    """
    print(sentence.splitlines())
    lst = []
    for line in sentence.splitlines():
        lst.append(line.strip())
    print(lst)
    print()

    # Python encoding\decoding
    print("résumé".encode("utf-8"))
    print(b"r\xc3\xa9sum\xc3\xa9".decode("utf-8"))
    print()
    letters = "αβγδ"
    raw_data = letters.encode("utf-8")
    print(raw_data.decode("utf-8"))
    print(raw_data.decode("utf-16"))
    print()
    print(len(letters.encode("utf-8")))
    print(len(letters.encode("utf-16")))

if __name__ == '__main__':
    run()
