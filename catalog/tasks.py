from django.db.models import signals
from celery import shared_task
from catalog.book import query_book_info
from catalog.models import Book, Publisher, Author, sync_book_data
from ownership.models import UserBook
from celery import chain
from datetime import datetime

@shared_task
def fetch_and_update_book_info_task(isbn):
    (query_book_info_task.s(isbn) | update_book_info_task.s(isbn)).apply_async()

@shared_task
def query_book_info_task(isbn):
    return query_book_info(isbn)

@shared_task
def update_book_info_task(book_dict, isbn):
    """
    Save a dictionary with the following format into database.
    Some fields may be ommitted to fit into the db fields.
    
    Book Dictionary format: {
        'annotation': 'url',
        'authors': [str],
        'date': 'yyyy-mm-dd'
        'description': 'str',
        'embeddability': 'str',
        'format': 'str'
        'identifiers': [
            ('google_id', 'value'), 
            ('ISBN', 'isbn13'),
            ('ISBN', 'isbn10'],
        'info': 'url',
        'preview': 'url',
        'publishers': ['str'],
        'subjects': ['str'],
        'thumbnail': 'url',
        'title': "str",
        'viewability': 'str'
    }"""

    if book_dict:

        book = Book.objects.get(isbn13=isbn)

        for author_name in book_dict.get('authors'):
            author, created = Author.objects.get_or_create(name=author_name)
            book.authors.add(author)

        for publisher_name in book_dict.get('publishers'):
            publisher, created = Publisher.objects.get_or_create(name=publisher_name)
            book.publishers.add(publisher)

        book.title = book_dict.get('title')
        book.description = book_dict.get('description')

        signals.post_save.disconnect(sync_book_data, sender=Book)
        book.save()
        signals.post_save.connect(sync_book_data, sender=Book)

