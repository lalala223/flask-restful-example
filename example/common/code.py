# -*- coding: utf-8 -*-


class Code(object):
    """自定义状态码类"""
    OK = 0
    DB_ERROR = 4001
    PARAM_ERROR = 4101
    AUTHORIZATION_ERROR = 4201
    UNKNOWN_ERROR = 4301


CODE_MSG_MAP = {
    Code.OK: 'ok',
    Code.DB_ERROR: '数据库错误',
    Code.PARAM_ERROR: '请求参数错误',
    Code.AUTHORIZATION_ERROR: '认证授权错误',
    Code.UNKNOWN_ERROR: "未知错误"
}
