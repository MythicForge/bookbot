from stats import *
import sys



def main():
    ###############################
    ## Function to open the text ##
    ###############################
    

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]

    def get_book_text(book_path):
        with open(book_path) as book:
            book_content = book.read()
        return book_content
    
    
    ######################
    ## Stats for Report ##
    ######################
    current_book = get_book_text(book)
    wc = get_book_wc(current_book)
    letters = get_unique_letters(current_book)
    
    sorted_list = merge_split_dict(letters)
    
    #print(sorted_list)
    ################################
    ## Print Report in formatting ##
    ################################
    def get_book_stats(letters, word_count):
        l_data = letters                
    # Print Format    
        print('============ BOOKBOT ============')    
        print(f'Analyzing book found at {book}...')
        print('----------- Word Count ----------')
        print(f'Found {word_count} total words')
        print('--------- Character Count -------')
        for pair in l_data:
            print(f'{pair["char"]}: {pair["num"]}')
        print("============= END ===============")
    get_book_stats(sorted_list, wc)

main()

