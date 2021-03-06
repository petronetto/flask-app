#!/usr/bin/env sh

printf "\n"
echo "--------------------------------------------------------------------"
echo "Checking CPU Cores to canculate workers"
echo "--------------------------------------------------------------------"
# (2 * cores) + 1
if [[ -f /proc/cpuinfo ]]; then
    workers=$(($((2 * ($(cat /proc/cpuinfo | grep processor | wc -l)))) + 1))
else
    workers=4
fi

printf "\n"
echo "--------------------------------------------------------------------"
echo "Using $workers Wokers"
echo "--------------------------------------------------------------------"

printf "\n"
echo "--------------------------------------------------------------------"
echo "Starting application"
echo "--------------------------------------------------------------------"
if [[ $PORT ]]; then
    gunicorn -w $workers -k gevent -b 0.0.0.0:$PORT app.wsgi:app
else
    gunicorn -w $workers -k gevent -b 0.0.0.0:5000 app.wsgi:app
fi
