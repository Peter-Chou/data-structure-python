#!/usr/bin/bash

pathargs=$(/cygdrive/c/cygwin/bin/find * -name "*.py" | sed 's@/@\\@g')
when-changed -1 $pathargs -c pytest -v -s "$@"