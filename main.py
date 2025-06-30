import sys
from stats import get_num_words
from stats import character_tracker
from stats import sort_on

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")

def main():
    book_path = sys.argv[1]
    words = get_num_words(book_path)
    print(f"Found {words} total words")
    character_dict = character_tracker(book_path)
    sorted_dict = sort_on(character_dict)
    # print(character_dict)
    print(sorted_dict)


main()