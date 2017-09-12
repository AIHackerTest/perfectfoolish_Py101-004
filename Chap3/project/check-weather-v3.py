# -*- coding: utf-8 -*-
"""
    Query the weather
    ~~~~~~
    The application to query the weather from internet.
    :copyright: (c) 2017 by Fulei.
    :license: BSD, see LICENSE for more details.
"""

import sys
import requests
import json
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators
from utils.const_value import API, KEY, UNIT, LANGUAGE

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

user_query_weather_history = []

class ReusableForm(Form):
    name = TextField('城市:', validators=[validators.required()])

def fetch_weather(location):
    result = requests.get(API, params = {
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout = 1)
    if result.status_code == requests.codes.ok:
        parsed_json = json.loads(result.text)
        raw_weather_data = parsed_json['results'][0]
        raw_time_data = raw_weather_data['last_update']
        process_weather_data = raw_weather_data['location']['name'] + ' ' + raw_weather_data['now']['text'] + ' ' + raw_weather_data['now']['temperature'] + '度' + ' ' + '风向' + raw_weather_data['now']['wind_direction']
        process_time_data = raw_time_data.split('T')[0] + ' ' + raw_time_data.split('T')[1].split('+')[0]
        user_query_weather_history.append(process_weather_data)

        my_weather_data = [process_weather_data, process_time_data]
        return my_weather_data
    else:
        warning_info = '暂时不支持您查询的城市'
        return warning_info

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name=request.form['name']
        if form.validate():
            flash(fetch_weather(name))
        else:
            flash('请输入城市名')

    return render_template('index.html', form=form)

@app.route("/help")
def user_help():
    return render_template('help.html')

@app.route("/history")
def history():
    flash(user_query_weather_history)
    return render_template('history.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
