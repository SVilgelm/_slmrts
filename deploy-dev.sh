#!/bin/sh
set -e
ROOT=`dirname "${BASH_SOURCE[0]}"`

# example: HOST=myserver.com
HOST=sladkiji-mir-tsvetov.ru

if [ -z "$HOST" ]; then
    echo "Setup HOST variable in $0!"
    exit 1
fi

NAME=slmrts
PROJECT_ROOT=/var/www/$NAME
VENV=$PROJECT_ROOT/system/venv
USER=www-data
GROUP=www-data

DEB=`tr '\n' ' ' < $ROOT/system/debian.txt`

echo "[`date +%H:%M:%S`] prepare"
ssh -t $HOST "\
    sudo apt-get install -y $DEB &&\
    sudo mkdir -p $PROJECT_ROOT $VENV &&\
    sudo chown -R \`whoami\`:$GROUP $PROJECT_ROOT &&\
    sudo chmod u+w $PROJECT_ROOT &&\
    true"

echo "[`date +%H:%M:%S`] copy files"
rsync $ROOT --recursive -F $HOST:$PROJECT_ROOT

echo "[`date +%H:%M:%S`] run postinstall"
#    sudo $PROJECT_ROOT/upgrade-requirements.sh &&\
ssh -t $HOST "\
    sudo find $PROJECT_ROOT -name \*.sh -type f -exec chmod +x {} \; &&\
    sudo chmod +x $PROJECT_ROOT/src/manage.py &&\
    sudo $PROJECT_ROOT/venv.sh &&\
    sudo chown -R $USER:$GROUP $PROJECT_ROOT &&\
    sudo $PROJECT_ROOT/system/postinstall.sh &&\
    true"

echo "[`date +%H:%M:%S`] done"
