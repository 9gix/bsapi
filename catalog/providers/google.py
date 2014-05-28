import urllib.request
import json


SERVER_URL = "www.googleapis.com"
RESOURCE_URL = "/books/v1/volumes"

class BookService(object):
    def search(query):
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf8')
        return json.loads(content)

class Book(object):
    def __init__(self, isbn13, title, *args, **kwargs):
        self.isbn13 = isbn13
        self.title = title

class Author(object):
    def __init__(self, name):
        self.name = name

class Publisher(object):
    def __init__(self, name):
        self.name = name
