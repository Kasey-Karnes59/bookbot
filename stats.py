def num_of_words(book_text):
	word_count = len(book_text.split())
	return word_count


def num_of_char(book_text):
	char_count = {}
	for i in book_text:
		i = i.lower()
		if i in char_count:
			char_count[i] += 1
		else:
			char_count[i] = 1
	return char_count

def sort_on(item):
	return item["num"]
	


def get_sorted_char_list(char_count):
	new_sorted_list = []
	for character, count in char_count.items():
		new_sorted_list.append({"char": character, "num": count})
		
	new_sorted_list.sort(reverse=True, key=sort_on)
	return new_sorted_list



	 




