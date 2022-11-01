from flask import Flask, render_template
from flask_caching import Cache
import pandas as pd
from skaters import get_skater_data_by_id, get_skater_data_by_team_id

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
    DATA = get_skater_data_by_team_id([1,5,9])
    return render_template("index.html",
                            tables=[DATA.to_html(classes='data', header="true", table_id="skater_table")],
                            titles=DATA.columns.values)

@cache.cached(timeout=260, key_prefix='function')
def function():
    '''Caches the data that is updated every ~5 minutes.'''
    data = 5
    return data