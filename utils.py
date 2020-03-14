#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 4:59 下午
# @Author  : 严梓桓
# @Site    : https://github.com/Oliver-Yan-2019
# @File    : utils.py


from urllib import quote


def ascii_sorted(_data, url_encode=True):
    _keys = sorted(_data)
    _str = ''
    for _key in _keys:
        if _data[_key] is None:
            continue

        data_str = quote(str(_data[_key])) if url_encode else str(_data[_key])
        _str += ".".join(_key.split("_")) + '=' + data_str + '&'

    return _str[:-1]
