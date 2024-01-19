def main():
    path_to_file = './books/frankenstein.txt'
    print_report(path_to_file)


def print_report(path):
    dictionary = get_letter_ocurrences(path)
    sorted_keys = list(dictionary)
    sorted_keys.sort()
    print(f'--- Begin report of {path} ---')
    word_count = get_book_word_count(path)
    print(f'{word_count} words found in the document')
    for key in sorted_keys:
        print(f"The '{key}' character was found {dictionary[key]} times")
    print('--- End report ---')


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


def get_book_word_count(path):
    words = get_book_text(path).split()
    return len(words)


def get_book_lines(path):
    return get_book_text(path).split('\n')[:-1]


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
