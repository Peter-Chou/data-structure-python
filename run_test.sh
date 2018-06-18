#!/usr/bin/sh

# when-changed -1 -r * -c pytest -v -s $1

# /cygdrive/c/cygwin/bin/find * -name "*.py" | xargs -0 -I {} when-changed -1 -r {} -c pytest -v -s $1

pathargs=$(/cygdrive/c/cygwin/bin/find * -name "*.py" | sed 's@/@\\@g') # solve windows path
when-changed -1 -v $pathargs -c pytest -v -s $1