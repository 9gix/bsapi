from haystack import indexes
from catalog.models import BookProfile

class BookProfileIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    isbn13 = indexes.CharField(model_attr='isbn13')
    title = indexes.CharField(model_attr='title')
    subtitle = indexes.CharField(model_attr='subtitle')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return BookProfile

