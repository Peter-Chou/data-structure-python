#!/usr/bin/bash
# 第一个参数指定pytest 要跑的
# 第二个及其后都是when-changed 监控的文件

pathargs=$(/cygdrive/c/cygwin/bin/find * -name "*.py" | sed 's@/@\\@g')
when-changed -1 $pathargs -c pytest -v -s "$@"