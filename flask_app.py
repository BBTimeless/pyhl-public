from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache()

app.config["DEBUG"] = True
app.config["CACHE_TYPE"] = 'simple'

cache.init_app(app)

'''
Renders the index template and passes in the launch information.
'''
@app.route('/')
def index():
    return render_template("index.html")

@cache.cached(timeout=260, key_prefix='function')
def function():
    '''Caches the data that is updated every ~5 minutes.'''
    data = 
    return data