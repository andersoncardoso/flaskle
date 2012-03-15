# What is?

 This is a small monkey patch on flask.Flask() to add bottle-like decorators for get/post/delete/put

# Instalation?

<pre>
pip install flaskle
</pre>

# Usage
<pre>
from flask import Flask
import flaskle

flaskle.patch()
app = Flask(__name__)

@app.get('/feature/')
def feature_get():
    # ... your 'get' view here
    return my_get_return

@app.post('/feature/')
def feature_post():
    # ...your 'post' view here
    return my_post_return

@app.put('/feature/')
def feature_put():
    # ...your 'put' view here
    return my_put_return

@app.delete('/feature/')
def feature_delete():
    # ...your 'delete' view here
    return my_delete_return

@app.get('/other/one/')
@app.post('/other/one/')
def get_and_post_view():
    # view code here
    return {'some': 'thing'}

if __name__ == '__main__':
    app.run()
</pre>
