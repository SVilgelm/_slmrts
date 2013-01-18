#!/bin/bash
set -e
ROOT=`dirname "${BASH_SOURCE[0]}"`
export DJANGO_SETTINGS_MODULE=slmrts.localsettings
$ROOT/venv.sh src/manage.py syncdb
$ROOT/venv.sh src/manage.py runserver
