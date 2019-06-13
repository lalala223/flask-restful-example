# * coding: utf8 *
import os
import unittest
import app
import manager
import flask_migrate


class TestApp(unittest.TestCase):

    def setUp(self):
        app_ctx = manager.app.app_context()
        app_ctx.push()
        flask_migrate.init()
        flask_migrate.migrate()
        flask_migrate.upgrade()
        app_ctx.pop()
        manager.app.config['TESTING'] = True
        self.client = manager.app.test_client()

    def tearDown(self):
        os.system('rm -rf ./migrations')
        os.system('rm -f ./example.db')

    def test_profiles(self):
        # post '/api/v1/profiles'
        req_route = '/api/v1/profiles'
        req_json = {'nickname': 'test', 'signature': 'test'}
        resp_json = {'code': 0, 'msg': 'ok', 'data': None}
        resp = self.client.post(req_route, json=req_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.get_json(), resp_json)

        # get '/api/v1/profiles'
        req_route = '/api/v1/profiles'
        resp_json = {
            'code': 0,
            'msg': 'ok',
            'data': {'items': [{'id': app.hash_ids.encode(1),
                                'nickname': 'test',
                                'signature': 'test'}],
                     'page_num': 1,
                     'page_size': 10,
                     'total': 1}
        }
        resp = self.client.get(req_route)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.get_json(), resp_json)

        # put '/api/v1/profiles/<id>'
        req_route = '/api/v1/profiles/{0}'.format(app.hash_ids.encode(1))
        req_json = {'nickname': 'hello', 'signature': 'hello'}
        resp_json = {'code': 0, 'msg': 'ok', 'data': None}
        resp = self.client.put(req_route, json=req_json)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.get_json(), resp_json)

        # get '/api/v1/profiles/<id>'
        req_route = '/api/v1/profiles/{0}'.format(app.hash_ids.encode(1))
        resp_json = {'code': 0,
                     'msg': 'ok',
                     'data': {'id': app.hash_ids.encode(1),
                              'nickname': 'hello',
                              'signature': 'hello'}
                     }
        resp = self.client.get(req_route)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.get_json(), resp_json)

        # delete '/api/v1/profiles/<id>'
        req_route = '/api/v1/profiles/{0}'.format(app.hash_ids.encode(1))
        resp_json = {'code': 0, 'msg': 'ok', 'data': None}
        resp = self.client.delete(req_route)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content_type, 'application/json')
        self.assertEqual(resp.get_json(), resp_json)


if __name__ == '__main__':
    unittest.main()
