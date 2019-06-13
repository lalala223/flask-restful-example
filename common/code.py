# -*- coding: utf-8 -*-

OK = 0

DB_ERROR = 4001

PARAM_ERROR = 4101

AUTHORIZATION_ERROR = 4201

UNKNOWN_ERROR = 4301

CODE_MSG_MAP = {
    OK: 'ok',
    DB_ERROR: '数据库错误',
    PARAM_ERROR: '请求参数错误',
    AUTHORIZATION_ERROR: '认证授权错误',
    UNKNOWN_ERROR: "未知错误"
}
