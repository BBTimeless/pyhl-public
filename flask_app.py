from flask import Flask, render_template, request
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
    return render_template("index.html")

@app.route('/skater/', methods=('GET', 'POST'))
def skater():
    if request.method == 'GET':
        DATA = get_skater_data_by_team_id([15])
        return render_template('skater_result.html',
                                tables=[DATA.to_html(classes='data', header="true", table_id="skater_table")],
                                titles=DATA.columns.values)

@cache.cached(timeout=260, key_prefix='function')
def function():
    '''Caches the data that is updated every ~5 minutes.'''
    data = 5
    return data