
def get_word_count(book_text):
    lst = book_text.split()
    return len(lst)

def create_symbol_dict(book_text):
    symbol_dict = {}
    for symbol in book_text:
        if symbol.lower().isalpha():
            if symbol.lower() in symbol_dict:
                symbol_dict[symbol.lower()] += 1
            else:
                symbol_dict[symbol.lower()] = 1
    return symbol_dict

def creating_dict_list(symbol_dict):
    dict_list = []
    for key in symbol_dict:
        dict_list.append({"char": key, "num": symbol_dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]