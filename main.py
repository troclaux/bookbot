def main():
    path_to_file = './books/frankenstein.txt'
    # lines = get_book_lines(path_to_file)
    print('word count:', get_book_words(path_to_file))
    print('letter dictionary:', get_letter_ocurrences(path_to_file))


def get_letter_ocurrences(path):
    lowercase_str = get_book_text(path).lower()
    lowercase_words = lowercase_str.split()
    output = dict()
    for word in lowercase_words:
        for char in word:
            if char in output:
                output[char] += 1
            else:
                output[char] = 1
    return output


def get_book_words(path):
    words = get_book_text(path).split()
    return len(words)


def get_book_lines(path):
    return get_book_text(path).split('\n')[:-1]


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
