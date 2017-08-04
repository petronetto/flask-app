#!/usr/bin/env sh

procs=$(cat /proc/cpuinfo | grep processor | wc -l)

gunicorn -w $procs -b 0.0.0.0:5000 app.main:app