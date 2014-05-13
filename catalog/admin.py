from django.contrib import admin
from catalog.models import BookProfile, Author, Publisher

admin.site.register(BookProfile)
admin.site.register(Author)
admin.site.register(Publisher)
