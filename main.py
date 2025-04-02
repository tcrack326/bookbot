from stats import get_num_words
from stats import get_character_count
from stats import get_sorted_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    [_, bookpath] = sys.argv
    contents = get_book_text(bookpath)
    num_words = get_num_words(contents)
    character_count = get_character_count(contents)
    sorted_count = get_sorted_dict(character_count)

    print(f'''
    ============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
''')
    for item in sorted_count.items():
        print(f'{item[0]}: {item[1]}')
    print('============= END ===============')

main()