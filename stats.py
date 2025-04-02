def get_num_words(text):
    return len(text.split())

CHAR_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
def get_character_count(text):
    lower_text = text.lower()
    character_dict = {letter: (lower_text.count(letter) or 0) for i, letter in enumerate(CHAR_LIST)}
    return character_dict

def get_sorted_dict(character_count_dict):
   sorted_items = sorted(character_count_dict.items(), reverse=True, key=lambda item: item[1])
   return dict(sorted_items)