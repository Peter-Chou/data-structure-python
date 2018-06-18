#!/usr/bin/bash

# when-changed -v -1 "${@:1}" -c pytest -v -s $1    # receive watch files start from second arg
# when-changed -1 -r * -c pytest -v -s $1
# /cygdrive/c/cygwin/bin/find * -name "*.py" | xargs -0 -I {} when-changed -1 -r {} -c pytest -v -s $1

pathargs=$(/cygdrive/c/cygwin/bin/find * -name "*.py" | sed 's@/@\\@g')
when-changed -1 $pathargs -c pytest -v -s "$@"