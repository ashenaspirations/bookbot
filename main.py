from stats import get_num_words
from stats import character_tracker
from stats import sort_on


def main():
    words = get_num_words("./books/frankenstein.txt")
    print(f"Found {words} total words")
    character_dict = character_tracker("./books/frankenstein.txt")
    sorted_dict = sort_on(character_dict)
    # print(character_dict)
    print(sorted_dict)


main()