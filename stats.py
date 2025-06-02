
#####################################
## Collect word count from content ##
#####################################
def get_book_wc(content):
    words = content.split()
    wc_tracker = 0
    for count in words:
        wc_tracker += 1
    print(f'{wc_tracker} words found in the document')