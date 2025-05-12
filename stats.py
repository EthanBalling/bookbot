def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        #print(text)
    return book_text
        
def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words
         
def get_num_chars(book_text):
    num_chars = {}
    for char in book_text.lower():
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def get_sorted_chars(num_chars):
    sorted_chars = []
    
    def sort_key(item):
        return item["count"]
    
    for char, count in num_chars.items():
        sorted_chars.append({"char": char, "count": count})
        
    sorted_chars.sort(key=sort_key, reverse=True)
    return sorted_chars
        
    