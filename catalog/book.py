from gdata.books.service import BookService


def query_book_info(isbn):
    """Retrieve a book info that matches with the ISBN provided"""
    def match_isbn(book):
        """Book Identifiers: (key,val)
            [('google_id', 'dwSfGQAACAAJ'),
            ('ISBN', '0132350882'),
            ('ISBN', '9780132350884')]"""
        ids = [ids_keyval[1] for ids_keyval in book.get('identifiers', [])]
        return isbn in ids 

    # GET https://www.googleapis.com/books/v1/volumes?q=isbn:<ISBN>
    service = BookService()
    result = service.search('isbn:' + isbn)

    result_dict = map(lambda entry: entry.to_dict(), result.entry)
    match_results = filter(match_isbn, result_dict)

    return match_results[0] if match_results else None

def search_book(query):
    service = BookService()
    result = service.search(query)
    return map(lambda entry: entry.to_dict(), result.entry)

