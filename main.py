import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(path):
	with open(path) as f:
		text = f.read()
		return text

def main():
	if len(sys.argv) ==2:
		path = sys.argv[1]
		text = get_book_text(path)

		num_words = count_words(text)
		char_counts = count_characters(text)
		sorted_chars = sort_characters(char_counts)

		print("============ BOOTBOT ============")
		print(f"Analyzing book found at {path}...")
		print("----------- Word Count -----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count ---------")

		for item in sorted_chars:
			print(f"{item['char']}: {item['num']}")

		print("============ END ============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)


main()
