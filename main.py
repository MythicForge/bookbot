from stats import get_book_wc

def main():
    
    def get_book_text(book_path):
        with open(book_path) as book:
            book_content = book.read()
        return book_content
    current_book = get_book_text("books/frankenstein.txt")
    get_book_wc(current_book)

main()