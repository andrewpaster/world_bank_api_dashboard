from worldbankapp import app

import json, plotly
from flask import render_template, request, Response, jsonify
from scripts.data import return_figures


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():

	if (request.method == 'POST'):
		figures = return_figures(request.form)
	else:
		figures = return_figures()

	# see: https://github.com/plotly/plotlyjs-flask-example/blob/master/app.py
	# add ids to each figure
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	# List of countries for filter
	country_codes = [['Canada','CAN'],['United States','USA'],['Brazil','BRA'],
	['France','FRA'],['India','IND'],['Italy','ITA'],['Germany','DEU'],
	['United Kingdom','GBR'],['China','CHN'],['Japan','JPN']]

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON,
		countries=country_codes)