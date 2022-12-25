# !/usr/bin/env python
# -*-coding:utf-8 -*-
'''
do download video
@:param url
@:return content
'''

import requests
import typing


def downloader(url: str, headers: str):
    # headers = headers

    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        return res.content
    else:
        return False
    # return content
