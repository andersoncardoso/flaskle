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
</pre>
