from django.contrib import admin
from catalog.models import (
        BookProfile,
        Author,
        Publisher,
        Category)

admin.site.register(BookProfile)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
