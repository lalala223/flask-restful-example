# -*- coding: utf-8 -*-
import hashlib
from .code import CODE_MSG_MAP


def pretty_result(code, msg=None, data=None):
    if msg is None:
        msg = CODE_MSG_MAP.get(code)
    return {
        'code': code,
        'msg': msg,
        'data': data
    }


def hash_md5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()
