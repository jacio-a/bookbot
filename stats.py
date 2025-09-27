
def num_words(text):
    num = text.split()
    return len(num)

def character_count(text):
    char_dict = {}
    word_list = text.split()
    for word in word_list:
        word_chars = [*word.lower()]
        for char in word_chars:
            if (char in char_dict) and char.isalpha():
                char_dict[char] += 1
            elif char.isalpha():
                char_dict[char] = 1
            else:
                continue
    return char_dict


def sort_on(char_dict):
    return char_dict["val"]

def sort_dict_into_list(char_dict):
    char_dict_list = []
    for char, val in char_dict.items():
        char_dict_list.append(dict(char = char, val = val))
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list

def print_sorted_char_dict(char_dict):
    sorted_char_dict = sort_dict_into_list(char_dict)
    for item in sorted_char_dict:
        print(f"{item["char"]}: {item["val"]}")
