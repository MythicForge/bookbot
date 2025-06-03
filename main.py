import sys

###############################
## Function to open the text ##
###############################
def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as f:
        return f.read()


######################
## Stats for Report ##
######################
# (You said you had these functions elsewhere—just stubbing them out here.)
def get_book_wc(text):
    """Return the total word count of `text`."""
    # e.g. simple split on whitespace:
    return len(text.split())


def get_unique_letters(text):
    """Return a dict mapping each character to its count."""
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def merge_split_dict(letter_dict):
    """
    Take a dict {char: count, …} and return a list of
    { 'char': <letter>, 'num': <count> } sorted however you like.
    """
    return [{'char': k, 'num': letter_dict[k]} for k in sorted(letter_dict)]


###############################
## Print Report in formatting ##
###############################
def get_book_stats(letter_list, word_count, book_path):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for pair in letter_list:
        print(f'{pair["char"]}: {pair["num"]}')
    print("============= END ===============")


def main():
    # Check “exactly one extra argument”:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    # Now we actually open/read/analyze:
    current_book = get_book_text(book)
    wc = get_book_wc(current_book)
    letters = get_unique_letters(current_book)
    sorted_list = merge_split_dict(letters)

    # Print the report
    get_book_stats(sorted_list, wc, book)


if __name__ == "__main__":
    main()
