#!/bin/bash

#define variable
NAME="PredictGender" # Name of the application
DJANGODIR=/var/www/PredictGender # Django project directory
SOCKFILE=/var/www/PredictGender/run/gunicorn.sock # we will communicte using this unix socket
USER=root # the user to run as
GROUP=root # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=Predictions.settings # which settings file should Django use
DJANGO_WSGI_MODULE=Predictions.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"


# Activate the virtual environment
cd $DJANGODIR
source ../../VENV/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR



# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /var/www/VENV/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=127.0.0.1:8000 \
--log-level=debug \
--log-file=-
