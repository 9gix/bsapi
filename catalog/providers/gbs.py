import urllib.request
import json


HTTP_PROTOCOL = 'https://'
SERVER_URL = "www.googleapis.com"
RESOURCE_URL = "/books/v1/volumes"

class BookService(object):
    def search(query):
        response = urllib.request.urlopen(HTTP_PROTOCOL + SERVER_URL+RESOURCE_URL+"?q={}".format(query))
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
