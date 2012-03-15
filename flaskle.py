# -*- coding: utf-8 -*-
"""
Decorators for Sinatra/Bottle like Rest apis

create great apis:

from flask import Flask
import flaskle

app = Flask(__name__)

@app.get('/feature/')
def feature_get():
    # ... sometinh here
    return something

@app.post('/feature/')
def feature_post():
    # ...some more things here
    return my_json_stuff

app.run()
"""
from flask import Flask, Blueprint

__version__ = "0.4"
__author__ = 'Anderson Pierre Cardoso'
__license__ = 'MIT'


def get(self, route, **options):
    """route using Http GET"""
    def wrapper(func):
        options['methods'] = ['GET', 'HEAD']
        self.add_url_rule(route, options.pop('endpoint', None), func, **options)
        return func
    return wrapper


def post(self, route, **options):
    """route using Http POST """
    def wrapper(func):
        options['methods'] = ['POST', 'HEAD']
        self.add_url_rule(route, options.pop('endpoint', None), func, **options)
        return func
    return wrapper


def put(self, route, **options):
    """route using Http PUT """
    def wrapper(func):
        options['methods'] = ['PUT', 'HEAD']
        self.add_url_rule(route, options.pop('endpoint', None), func, **options)
        return func
    return wrapper


def delete(self, route, **options):
    """route using Http DELETE """
    def decorator(f):
        options['methods'] = ('DELETE', 'HEAD')
        self.add_url_rule(route, options.pop('endpoint', None), f, **options)
        return f
    return decorator


# monkey patch everything
def patch():
    Flask.get = get
    Flask.post = post
    Flask.put = put
    Flask.delete = delete

    Blueprint.get = get
    Blueprint.post = post
    Blueprint.put = put
    Blueprint.delete = delete
