def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    word_count = count_words(text)
    character_dict = count_char(text)
    list_of_dicts = create_list_of_dicts(character_dict)

def open_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
        words = text.split()
        return len(words)
        
def count_char(text):
    character_dict = {}
    for char in text:
        lowered_string = char.lower()
        if lowered_string in character_dict:
             character_dict[lowered_string] += 1
        else:
             character_dict[lowered_string] = 1
    return character_dict

def create_list_of_dicts(dict):
    list_of_dicts = []
    for i in dict:
        if i.isalpha() == True:
            list_of_dicts.append({"letter": i, "instances":dict.get(i)})
    return list_of_dicts

def sort_on(dict):
     return dict["instances"]

book_path = "books/frankenstein.txt"
text = open_book(book_path)
word_count = count_words(text)
character_dict = count_char(text)
list_of_dicts = create_list_of_dicts(character_dict)
list_of_dicts.sort(reverse =True, key=sort_on)



print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print("")
for i in list_of_dicts:
    print(f'The {i["letter"]} character was found {i["instances"]} times ')
print("--- End report ---")
main()