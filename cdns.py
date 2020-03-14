#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 4:43 下午
# @Author  : 严梓桓
# @Site    : https://github.com/Oliver-Yan-2019
# @File    : cdns.py

import requests
import time
import random
import string
import hmac
import base64
from hashlib import sha256, sha1

from utils import ascii_sorted
from config.default_config import SecretId, SecretKey


def create_domain(domain="qcloud.com", project_id=0):
    """
    添加域名
    :param domain: 域名
    :type domain:
    :param project_id:
    :type project_id:
    :return:
    :rtype:
    """

    _requests_json = {
        "Action": "DomainCreate",
        "SecretId": SecretId,
        "Timestamp": int(time.time()),
        "Nonce": ''.join(random.sample(string.ascii_letters + string.digits, 8)),
        "SignatureMethod": "HmacSHA256",
        "domain": domain,
        "projectId": project_id,
    }

    _requests_url = "https://cns.api.qcloud.com/v2/index.php?{}".format(ascii_sorted(_requests_json))
    _signature = generate_signature(_data=_requests_url, _secret_key=SecretKey, _method="HmacSHA256")
    return requests.post(url=_requests_url + _signature)


def create_record(domain="qcloud.com", sub_domain="", record_type="", record_line="", value="", ttl=None, mx=None):
    """
    添加解析记录
    :param domain:
    :type domain:
    :param sub_domain:
    :type sub_domain:
    :param record_type:
    :type record_type:
    :param record_line:
    :type record_line:
    :param value:
    :type value:
    :param ttl:
    :type ttl:
    :param mx:
    :type mx:
    :return:
    :rtype:
    """

    _requests_json = {
        "Action": "RecordCreate",
        "SecretId": SecretId,
        "Timestamp": int(time.time()),
        "Nonce": ''.join(random.sample(string.ascii_letters + string.digits, 8)),
        "SignatureMethod": "HmacSHA256",
        "domain": domain,
        "subDomain": sub_domain,
        "recordType": record_type,
        "recordLine": record_line,
        "value": value,
        "ttl": ttl,
        "mx": mx,
    }

    _requests_url = "https://cns.api.qcloud.com/v2/index.php?{}".format(ascii_sorted(_requests_json))
    _signature = generate_signature(_data=_requests_url, _secret_key=SecretKey, _method="HmacSHA256")
    return requests.post(url=_requests_url + _signature)


def generate_signature(_data="", _secret_key="", _method="HmacSHA256"):
    if _method == "HmacSHA256":
        _digest = hmac.new(
            _secret_key,
            _data,
            sha256
        ).digest()
        return base64.b64encode(_digest)
    else:
        _digest = hmac.new(
            _secret_key,
            _data,
            sha1
        ).digest()
        return base64.b64encode(_digest)


if __name__ == "__main__":
    create_domain()
