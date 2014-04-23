quizbowl
========

quizbowl software repository

Installation
-----

You'll need a postgresql server set up. Create a database named "quizbowl" and a user
named "quizbowl" with the password, you guessed it, "quizbowl." Run 

    python manage.py syncdb

in the root of the project. It should create the necessary admin tables and such.
