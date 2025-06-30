def get_num_words(filepath):
    file_contents = ""
    word_count = 0
    with open(filepath) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            word_count += 1
        return word_count


def character_tracker(path_to_file):
    char_count = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        }
    
    complete_string = ""
    with open(path_to_file) as f:
        complete_string = f.read()
        for char in complete_string.lower():
            if char in char_count:
                char_count[char] += 1
        return char_count
    

def sort_on(character_dict):
    char_list = [{"char": letter, "num": count} for letter, count in character_dict.items()]
    sorted_list = sorted(char_list, key=lambda item: item["num"], reverse=True)

    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")