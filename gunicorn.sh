#!/usr/bin/bash

cd /home/arthur/adenblack
pipenv run gunicorn adenblack.wsgi:application
