import sys
from stats import get_book_words
from stats import get_chars
from stats import get_sorted_chars
from stats import sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_book_words(text)
    chars = get_chars(text)
    report = get_sorted_chars(chars)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    print(f"{report}")
    print(f"============= END ===============")

main()