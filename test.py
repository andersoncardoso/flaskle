# -*- coding: utf-8 -*-
import unittest
from flask import Flask
import flaskle

app = Flask(__name__)

@app.get('/test/')
def _get_view():
    return 'GET TEST'

@app.post('/test/')
def _post_view():
    return 'POST TEST'

@app.put('/test/')
def _put_view():
    return 'PUT TEST'

@app.delete('/test/')
def _delete_view():
    return 'DELETE TEST'


class FlaskleTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get(self):
        r = self.app.get('/test/')
        assert 'GET TEST' in r.data

    def test_post(self):
        r = self.app.post('/test/')
        assert 'POST TEST' in r.data

    def test_put(self):
        r = self.app.put('/test/')
        assert 'PUT TEST' in r.data

    def test_delete(self):
        r = self.app.delete('/test/')
        assert 'DELETE TEST' in r.data



if __name__ == '__main__':
    unittest.main()