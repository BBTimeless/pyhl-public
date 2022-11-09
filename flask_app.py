from flask import Flask, render_template, request, redirect, url_for
from flask_caching import Cache
import pandas as pd
from skaters import get_skater_data_by_id, get_skater_data_by_team_id, get_top_skaters
from teams import get_team_data_all
from schedule import get_teams_playing_today

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
    SKATER_DATA = get_skater_data_by_team_id(get_teams_playing_today())
    return render_template('index.html',
                            skaters = SKATER_DATA,
                            headers = SKATER_DATA.columns
                            # skater_tables=[SKATER_DATA.to_html(classes='data', header="true", table_id="skater_table")],
                            # skater_titles=[SKATER_DATA.columns.values]
                            )

'''
Renders the skater template with the selection form.
'''
@app.route('/skater/')
def skater():
    TEAMS_DATA = get_team_data_all()
    return render_template("skater.html",
                            teams = TEAMS_DATA)

'''
Renders the results from the skater form into a table.
'''
@app.route('/skater_results/', methods=('GET', 'POST'))
def skater_results():
    if request.method == 'POST':
        form_data = request.form.getlist('team')
        ids = [eval(i) for i in form_data]
        SKATER_DATA = get_skater_data_by_team_id(ids)
        return render_template('skater_results.html',
                                skater_tables=[SKATER_DATA.to_html(classes='data', header="true", table_id="skater_table")],
                                skater_titles=[SKATER_DATA.columns.values]
        )
                                
    else:
        return redirect(url_for('index'))

@cache.cached(timeout=260, key_prefix='function')
def function():
    '''Caches the data that is updated every ~5 minutes.'''
    data = 5
    return data