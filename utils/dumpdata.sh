#!/bin/bash

# Please ensure that the dump file is small (fixtures/dump_data.json)
# by deleting unrelated books, category, publisher, author

# These are the django shell commands to remove those data before dump it into json
# > Book.objects.filter(userbook__isnull=True).delete()
# > Author.objects.filter(book__isnull=True).delete()
# > Publisher.objects.filter(book__isnull=True).delete()
# > Category.objects.filter(book__isnull=True).delete()

python manage.py dumpdata auth.user catalog.book catalog.category catalog.author catalog.publisher ownership.userbook sites.site --indent=4 > fixtures/dump_data.json
