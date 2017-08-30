#!/usr/bin/env sh

# (2 * cores) + 1
workers=$(($((2 * ($(cat /proc/cpuinfo | grep processor | wc -l)))) + 1))

if [[ $PORT ]]; then
    gunicorn -w $workers -k gevent -b 0.0.0.0:$PORT app.wsgi:app
else
    gunicorn -w $workers -k gevent -b 0.0.0.0:5000 app.wsgi:app
fi
