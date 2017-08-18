#!/usr/bin/env sh

procs=$(cat /proc/cpuinfo | grep processor | wc -l)

if [ "${PORT}" ]; then
    gunicorn -w $procs -b 0.0.0.0:$PORT app.wsgi:app
else
    gunicorn -w $procs -b 0.0.0.0:5000 app.wsgi:app
fi