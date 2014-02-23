from gdata.books.service import BookService
from catalog.models import Book


def query_book_info(isbn):
    """Retrieve a book info that matches with the ISBN provided"""
    def match_isbn(book):
        """Book Identifiers: (key,val)
            [('google_id', 'dwSfGQAACAAJ'),
            ('ISBN', '0132350882'),
            ('ISBN', '9780132350884')]"""
        ids = [ids_keyval[1] for ids_keyval in book.get('identifier', [])]
        return isbn in ids 

    service = BookService()
    result = service.search(isbn)

    result_dict = [book.to_dict() for book in result.entry]
    match_results = filter(match_isbn, result_dict)

    return match_results[0] if match_results else None
