def main():
    path_to_file = './books/frankenstein.txt'
    # lines = get_book_lines(path_to_file)
    word_count = get_book_words(path_to_file)
    print(word_count)


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
