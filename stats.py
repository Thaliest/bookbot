def count_words(text):
	words = text.split()
	total_count = len(words)
	return total_count

def count_characters(text):
	lower = text.lower()
	count_characters = {}
	for char in lower:
		if char in count_characters:
			count_characters[char] += 1
		else:
			count_characters[char] = 1
	return count_characters

def sort_characters(char_dict):
	char_list = [{"char": char, "num": count} for char, count in char_dict.items() if char.isalpha()]
	char_list.sort(key=lambda d: d["num"], reverse=True)
	return char_list
