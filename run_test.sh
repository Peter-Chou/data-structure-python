#!/usr/bin/bash
# 第一个参数指定pytest 要跑的
# 第二个及其后都是when-changed 监控的文件

# when-changed -v -1 "${@:1}" -c pytest -v -s $1
when-changed -1 -r * -c pytest -v -s $1
