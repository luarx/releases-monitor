#!/bin/sh

# -e -> If a command fails, set -e will make the whole script exit, instead of just resuming on the next line.
# -u -> Treat unset variables as an error, and immediately exit.
# -o pipefail -> Causes a pipeline (for example, curl -s http://sipb.mit.edu/ | grep foo) to produce a failure return code if any command errors. Normally, pipelines only return a failure if the last command errors.
set -euo pipefail

echo "==> Migrating Django models ... "
python manage.py migrate --noinput

echo "==> Collecting statics ... "
DOCKER_SHARED_DIR=/nginx
rm -rf $DOCKER_SHARED_DIR/*
STATIC_ROOT=$DOCKER_SHARED_DIR/staticfiles python manage.py collectstatic --noinput

echo "==> Running Gunicorn ... "
gunicorn --pythonpath "$PWD" releasesmonitor.wsgi:application --log-file=- --error-logfile=- --access-logfile '-' --log-level info -b unix:$DOCKER_SHARED_DIR/gunicorn.socket -b 0.0.0.0:8888 --worker-class gevent
