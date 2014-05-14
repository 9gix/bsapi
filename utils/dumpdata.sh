#!/bin/bash
python manage.py dumpdata auth.user catalog.bookprofile catalog.author catalog.publisher ownership.book --indent=4 > fixtures/dump_data.json
