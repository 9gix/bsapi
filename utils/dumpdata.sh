#!/bin/bash
python manage.py dumpdata auth.user catalog.book catalog.author catalog.publisher ownership.user_book --indent=4 > fixtures/dump_data.json
