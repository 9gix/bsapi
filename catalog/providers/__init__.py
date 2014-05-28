from catalog.providers import gbs

def search(query):
    book_list = gbs.BookService.search(query)
    return book_list
