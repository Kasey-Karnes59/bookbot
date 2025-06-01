import sys 
from stats import num_of_words
from stats import num_of_char
from stats import get_sorted_char_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents  

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at ...")
    print("----------- Word Count ----------")
    book_contents = get_book_text(sys.argv[1])
    word_count = num_of_words(book_contents)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = num_of_char(book_contents)
    sorted_char_list = get_sorted_char_list(char_counts)
    for item in sorted_char_list:
        character = item["char"]
        count = item["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")




    
    










main()
 

