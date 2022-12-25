'''
保存到临时目录
@:param
'''
# !/usr/bin/env python
# -*-coding:utf-8 -*-

#
import os
import typing


def save(content: typing.Any, filename: typing.Any, path="save"):
    if content is None:
        return None
    if os.path.exists(path):
        with open(filename, 'wb') as f:
            f.write(content)
