from flask import Flask, render_template
from flask_caching import Cache
import pandas as pd
from skaters import get_skater_data, get_skater_features

app = Flask(__name__)
cache = Cache()

app.config["DEBUG"] = True
app.config["CACHE_TYPE"] = 'simple'

cache.init_app(app)

'''
Renders the index template.
'''
@app.route('/')
def index():
    DATA = get_skater_data()
    return render_template("index.html",
                            tables=[DATA.to_html(classes='data', header="true")],
                            titles=DATA.columns.values)

@cache.cached(timeout=260, key_prefix='function')
def function():
    '''Caches the data that is updated every ~5 minutes.'''
    data = 5
    return data