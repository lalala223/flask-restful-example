# -*- coding: utf-8 -*-
from common.code import CODE_MSG_MAP


def pretty_result(code, msg=None, data=None):
    if msg is None:
        msg = CODE_MSG_MAP.get(code)
    return {
        'code': code,
        'msg': msg,
        'data': data
    }
