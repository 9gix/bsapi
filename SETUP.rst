Setup Guide
===========

This setup is not only about software installation but also about configuration.
It is recommended that you explore the software you install.

Prerequisite (General)
----------------------

You Don't Say?

#. `Setup Python 3`_
#. `Setup Git`_
#. `Setup VirtualEnv`_
#. `Setup VirtualEnvWrapper`_
#. `Setup Sqlite3`_
#. `Setup Pillow`_

Prerequisite (For Server)
----------------------

#. `Setup Redis`_
#. `Setup PostgreSQL`_
#. `Setup ElasticSearch`_


Installation for Developer
--------------------------

.. code-block:: sh

    # project virtual environment
    mkvirtualenv bsapi -p <path-to-python3-executable>
    workon bsapi

    # Clone project
    git clone git@github.com:9gix/bsapi.git

    cd bsapi

    # Install package dependencies
    pip install -r requirements/dev.txt

    # Create Database
    python manage.py migrate

    # Run Test
    python manage.py test

    # For Test Data on your local machine
    python manage.py loaddata fixtures/dump_data.json

    # Runserver
    python manage.py runserver

Installation for Server
-----------------------

.. code-block:: sh

    # Install package dependencies
    pip install -r requirements.txt

    # Run Server
    gunicorn bookshare.wsgi:application

Installation for Server (Ubuntu)
--------------------------------

.. code-block:: sh

    apt install postgresql-server-dev-X.Y postgresql postgresql-contrib
    apt install python3-dev
    apt install supervisor # process monitor & control



.. _Setup Python 3: https://wiki.python.org/moin/BeginnersGuide/Download
.. _Setup Git: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
.. _Setup VirtualEnv: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
.. _Setup VirtualEnvWrapper: http://virtualenvwrapper.readthedocs.org/en/latest/install.html
.. _Setup Sqlite3: http://www.sqlite.org/download.html
.. _Setup PostgreSQL: https://wiki.postgresql.org/wiki/Detailed_installation_guides
.. _Setup Redis: http://redis.io/download
.. _Setup ElasticSearch: http://www.elasticsearch.org/overview/elasticsearch/
.. _Setup Pillow: http://pillow.readthedocs.org/en/latest/installation.html
