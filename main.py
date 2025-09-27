
import sys
from stats import num_words
from stats import character_count
from stats import print_sorted_char_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}")
    book_contents = get_book_text(filepath)
    wordcount = num_words(book_contents)
    char_dict = character_count(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    print_sorted_char_dict(char_dict)


main()
