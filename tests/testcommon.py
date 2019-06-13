# -*- coding: utf-8 -*-
import unittest
from common import code, utils


class TestCode(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_code(self):
        self.assertEqual(code.OK, 0)
        self.assertEqual(code.DB_ERROR, 4001)
        self.assertEqual(code.PARAM_ERROR, 4101)
        self.assertEqual(code.AUTHORIZATION_ERROR, 4201)
        self.assertEqual(code.UNKNOWN_ERROR, 4301)


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pretty_result(self):
        result = utils.pretty_result(code.OK)
        self.assertEqual(result, {'code': 0, 'msg': 'ok', 'data': None})

    def test_hash_md5(self):
        result = utils.hash_md5('test'.encode())
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 32)

    def test_get_zodiac(self):
        result = utils.get_zodiac(11, 19)
        self.assertEqual(result, '天蝎座')

    def test_get_agr(self):
        result = utils.get_age(1993, 10, 6)
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()
