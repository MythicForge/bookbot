
#####################################
## Collect word count from content ##
#####################################
def get_book_wc(book):
    words = book.split()
    wc_tracker = 0
    for count in words:
        wc_tracker += 1
    return wc_tracker



#######################################
## Collect letter count from content ##
#######################################
def get_unique_letters(book):
    
    cased_letters = book.lower()
    filterd_letters = set("abcdefghijklmnopqrstuvwxyzæâêëô1234567890")
    which_letters = {}
    
    for letter in cased_letters:
        if letter in filterd_letters:
            if letter in which_letters:
                which_letters[letter] += 1
            else:
                which_letters[letter] = 1
        
    return which_letters


#######################################################
## Separate dictionary content of get_unique_letters ##
#######################################################

def merge_split_dict(dict1):
    new_list = []
    for lttr in dict1:
        if lttr.isalpha():
            new_dict = {"char": lttr, "num": dict1[lttr]}        
            new_list.append(new_dict)
    new_list.sort(key=lambda entry: entry["num"], reverse=True)
    return new_list
    
    

